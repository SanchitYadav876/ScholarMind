import React, { useState, useFocusEffect } from 'react';
import {
  View,
  ScrollView,
  Text,
  StyleSheet,
  ActivityIndicator,
  RefreshControl,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { predictionService } from '../services/predictionService';

export default function HistoryScreen() {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  useFocusEffect(
    React.useCallback(() => {
      loadHistory();
    }, [])
  );

  const loadHistory = async () => {
    try {
      setLoading(true);
      const history = await predictionService.getHistory();
      setPredictions(history);
    } catch (error) {
      console.error('Error loading history:', error);
      Alert.alert('Info', 'Using offline data (no server connection)');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await loadHistory();
  };

  const handleClearHistory = () => {
    Alert.alert(
      'Clear History',
      'Are you sure you want to clear all predictions?',
      [
        { text: 'Cancel', style: 'cancel' },
        {
          text: 'Delete',
          style: 'destructive',
          onPress: async () => {
            await predictionService.clearLocalData();
            setPredictions([]);
            Alert.alert('Success', 'History cleared');
          },
        },
      ]
    );
  };

  if (loading) {
    return (
      <View style={styles.centerContainer}>
        <ActivityIndicator size="large" color="#667eea" />
      </View>
    );
  }

  if (predictions.length === 0) {
    return (
      <View style={styles.centerContainer}>
        <MaterialCommunityIcons name="clipboard-list-outline" size={60} color="#ccc" />
        <Text style={styles.emptyText}>No predictions yet</Text>
        <Text style={styles.emptySubtext}>
          Go to Predictor tab to make predictions
        </Text>
      </View>
    );
  }

  return (
    <ScrollView
      style={styles.container}
      refreshControl={
        <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
      }
    >
      <View style={styles.content}>
        {/* Header with Clear Button */}
        <View style={styles.header}>
          <Text style={styles.headerTitle}>
            {predictions.length} Predictions
          </Text>
          <TouchableOpacity onPress={handleClearHistory}>
            <MaterialCommunityIcons name="delete" size={24} color="#dc3545" />
          </TouchableOpacity>
        </View>

        {/* Predictions List */}
        {predictions.map((prediction, index) => (
          <View key={prediction.id || index} style={styles.predictionCard}>
            {/* Top Section: Result Badge + Time */}
            <View style={styles.cardHeader}>
              <View
                style={[
                  styles.resultBadge,
                  prediction.prediction === 'PASS'
                    ? styles.passBadge
                    : styles.failBadge,
                ]}
              >
                <MaterialCommunityIcons
                  name={
                    prediction.prediction === 'PASS'
                      ? 'check-circle'
                      : 'close-circle'
                  }
                  size={16}
                  color={
                    prediction.prediction === 'PASS' ? '#28a745' : '#dc3545'
                  }
                />
                <Text
                  style={[
                    styles.badgeText,
                    {
                      color:
                        prediction.prediction === 'PASS'
                          ? '#28a745'
                          : '#dc3545',
                    },
                  ]}
                >
                  {prediction.prediction}
                </Text>
              </View>
              <Text style={styles.timestamp}>
                {new Date(prediction.timestamp).toLocaleString()}
              </Text>
            </View>

            {/* Student Data */}
            <View style={styles.dataGrid}>
              <View style={styles.dataItem}>
                <Text style={styles.dataLabel}>Marks</Text>
                <Text style={styles.dataValue}>
                  {prediction.marks.toFixed(1)}%
                </Text>
              </View>
              <View style={styles.dataItem}>
                <Text style={styles.dataLabel}>Attendance</Text>
                <Text style={styles.dataValue}>
                  {prediction.attendance.toFixed(1)}%
                </Text>
              </View>
              <View style={styles.dataItem}>
                <Text style={styles.dataLabel}>Study Hrs</Text>
                <Text style={styles.dataValue}>
                  {prediction.study_hours.toFixed(1)}h
                </Text>
              </View>
              <View style={styles.dataItem}>
                <Text style={styles.dataLabel}>Assignments</Text>
                <Text style={styles.dataValue}>
                  {prediction.assignments.toFixed(0)}/10
                </Text>
              </View>
            </View>

            {/* Probabilities */}
            <View style={styles.probabilities}>
              <View style={styles.probItem}>
                <Text style={styles.probLabel}>Pass</Text>
                <Text style={[styles.probValue, styles.passProb]}>
                  {prediction.pass_probability}%
                </Text>
              </View>
              <View style={styles.probItem}>
                <Text style={styles.probLabel}>Fail</Text>
                <Text style={[styles.probValue, styles.failProb]}>
                  {prediction.fail_probability}%
                </Text>
              </View>
            </View>
          </View>
        ))}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  content: {
    padding: 15,
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingBottom: 100,
  },
  emptyText: {
    fontSize: 18,
    fontWeight: '600',
    color: '#666',
    marginTop: 15,
  },
  emptySubtext: {
    fontSize: 14,
    color: '#999',
    marginTop: 8,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 15,
  },
  headerTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#333',
  },
  predictionCard: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginBottom: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 3,
    elevation: 3,
  },
  cardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
    paddingBottom: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#f0f0f0',
  },
  resultBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 20,
  },
  passBadge: {
    backgroundColor: '#d4edda',
  },
  failBadge: {
    backgroundColor: '#f8d7da',
  },
  badgeText: {
    fontSize: 12,
    fontWeight: '700',
    marginLeft: 6,
  },
  timestamp: {
    fontSize: 12,
    color: '#999',
  },
  dataGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 12,
  },
  dataItem: {
    width: '48%',
    backgroundColor: '#f9f9f9',
    padding: 10,
    borderRadius: 8,
    marginBottom: 8,
  },
  dataLabel: {
    fontSize: 11,
    color: '#999',
    marginBottom: 4,
  },
  dataValue: {
    fontSize: 14,
    fontWeight: '600',
    color: '#333',
  },
  probabilities: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: '#f0f0f0',
  },
  probItem: {
    flex: 1,
    alignItems: 'center',
  },
  probLabel: {
    fontSize: 12,
    color: '#999',
    marginBottom: 4,
  },
  probValue: {
    fontSize: 16,
    fontWeight: '700',
  },
  passProb: {
    color: '#28a745',
  },
  failProb: {
    color: '#dc3545',
  },
});
