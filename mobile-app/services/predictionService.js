import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Change this to your server URL
// For local development: http://localhost:5000 (won't work on physical device)
// For production: https://your-deployed-app.com

const API_BASE_URL = 'http://localhost:5000'; // Change to your deployed URL

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
});

export const predictionService = {
  // Make a prediction
  async predict(studentData) {
    try {
      const response = await api.post('/predict', studentData);
      
      // Save to local storage
      const predictions = await this.getLocalPredictions();
      const newPrediction = {
        id: Date.now(),
        timestamp: new Date().toISOString(),
        ...studentData,
        ...response.data,
      };
      predictions.push(newPrediction);
      await AsyncStorage.setItem('predictions', JSON.stringify(predictions));
      
      return response.data;
    } catch (error) {
      throw error.response?.data || { error: 'Failed to make prediction' };
    }
  },

  // Get statistics
  async getStatistics() {
    try {
      const response = await api.get('/statistics');
      return response.data;
    } catch (error) {
      // Return local stats if offline
      return this.getLocalStatistics();
    }
  },

  // Get prediction history
  async getHistory() {
    try {
      const response = await api.get('/history');
      return response.data.predictions;
    } catch (error) {
      // Return local history if offline
      return this.getLocalPredictions();
    }
  },

  // Local storage methods (for offline support)
  async getLocalPredictions() {
    try {
      const data = await AsyncStorage.getItem('predictions');
      return data ? JSON.parse(data) : [];
    } catch (error) {
      return [];
    }
  },

  async getLocalStatistics() {
    try {
      const predictions = await this.getLocalPredictions();
      if (predictions.length === 0) {
        return {
          total_predictions: 0,
          pass_count: 0,
          fail_count: 0,
          pass_rate: 0,
          avg_pass_probability: 0,
        };
      }

      const passCount = predictions.filter(p => p.prediction === 'PASS').length;
      const totalProb = predictions.reduce((sum, p) => sum + (p.pass_probability || 0), 0);

      return {
        total_predictions: predictions.length,
        pass_count: passCount,
        fail_count: predictions.length - passCount,
        pass_rate: (passCount / predictions.length * 100),
        avg_pass_probability: totalProb / predictions.length,
      };
    } catch (error) {
      return {
        total_predictions: 0,
        pass_count: 0,
        fail_count: 0,
        pass_rate: 0,
        avg_pass_probability: 0,
      };
    }
  },

  async clearLocalData() {
    try {
      await AsyncStorage.removeItem('predictions');
    } catch (error) {
      console.error('Error clearing local data:', error);
    }
  },
};
