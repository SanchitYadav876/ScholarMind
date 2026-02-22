import React, { useState } from 'react';
import {
  View,
  ScrollView,
  TouchableOpacity,
  Text,
  StyleSheet,
  TextInput,
  ActivityIndicator,
  Alert,
  Picker,
} from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { predictionService } from '../services/predictionService';

export default function PredictorScreen() {
  const [marks, setMarks] = useState('');
  const [studyHours, setStudyHours] = useState('');
  const [attendance, setAttendance] = useState('');
  const [previousMarks, setPreviousMarks] = useState('');
  const [assignments, setAssignments] = useState('');
  const [extracurricular, setExtracurricular] = useState('');
  const [parentalEducation, setParentalEducation] = useState('2');
  const [schoolType, setSchoolType] = useState('private');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handlePredict = async () => {
    // Validation
    if (!marks || !studyHours || !attendance || !previousMarks || !assignments || !extracurricular) {
      Alert.alert('Error', 'Please fill all fields');
      return;
    }

    const studentData = {
      marks: parseFloat(marks),
      study_hours: parseFloat(studyHours),
      attendance: parseFloat(attendance),
      previous_marks: parseFloat(previousMarks),
      assignments: parseFloat(assignments),
      extracurricular: parseFloat(extracurricular),
      parental_education: parseFloat(parentalEducation),
      school_type: schoolType,
    };

    try {
      setLoading(true);
      const response = await predictionService.predict(studentData);
      setResult(response);
    } catch (error) {
      Alert.alert('Error', error.error || 'Failed to make prediction');
    } finally {
      setLoading(false);
    }
  };

  const resetForm = () => {
    setMarks('');
    setStudyHours('');
    setAttendance('');
    setPreviousMarks('');
    setAssignments('');
    setExtracurricular('');
    setParentalEducation('2');
    setSchoolType('private');
    setResult(null);
  };

  return (
    <ScrollView style={styles.container}>
      <View style={styles.content}>
        {!result ? (
          <>
            <View style={styles.section}>
              <Text style={styles.sectionTitle}>Student Information</Text>

              <View style={styles.formGroup}>
                <Text style={styles.label}>Current Marks (%)</Text>
                <TextInput
                  style={styles.input}
                  placeholder="0-100"
                  keyboardType="decimal-pad"
                  value={marks}
                  onChangeText={setMarks}
                  maxLength={5}
                />
                <Text style={styles.hint}>Student's current score</Text>
              </View>

              <View style={styles.formGroup}>
                <Text style={styles.label}>Study Hours/Week</Text>
                <TextInput
                  style={styles.input}
                  placeholder="0-20"
                  keyboardType="decimal-pad"
                  value={studyHours}
                  onChangeText={setStudyHours}
                  maxLength={5}
                />
                <Text style={styles.hint}>Hours studying outside class</Text>
              </View>

              <View style={styles.formGroup}>
                <Text style={styles.label}>Attendance (%)</Text>
                <TextInput
                  style={styles.input}
                  placeholder="0-100"
                  keyboardType="decimal-pad"
                  value={attendance}
                  onChangeText={setAttendance}
                  maxLength={5}
                />
                <Text style={styles.hint}>Class attendance percentage</Text>
              </View>

              <View style={styles.formGroup}>
                <Text style={styles.label}>Previous Year Marks (%)</Text>
                <TextInput
                  style={styles.input}
                  placeholder="0-100"
                  keyboardType="decimal-pad"
                  value={previousMarks}
                  onChangeText={setPreviousMarks}
                  maxLength={5}
                />
                <Text style={styles.hint}>Last year's performance</Text>
              </View>

              <View style={styles.formGroup}>
                <Text style={styles.label}>Assignments Submitted</Text>
                <TextInput
                  style={styles.input}
                  placeholder="0-10"
                  keyboardType="decimal-pad"
                  value={assignments}
                  onChangeText={setAssignments}
                  maxLength={2}
                />
                <Text style={styles.hint}>Number of assignments done</Text>
              </View>

              <View style={styles.formGroup}>
                <Text style={styles.label}>Extracurricular Score</Text>
                <TextInput
                  style={styles.input}
                  placeholder="0-10"
                  keyboardType="decimal-pad"
                  value={extracurricular}
                  onChangeText={setExtracurricular}
                  maxLength={2}
                />
                <Text style={styles.hint}>Involvement in activities</Text>
              </View>

              <View style={styles.formGroup}>
                <Text style={styles.label}>Parental Education Level</Text>
                <View style={styles.pickerContainer}>
                  <Picker
                    selectedValue={parentalEducation}
                    onValueChange={setParentalEducation}
                    style={styles.picker}
                  >
                    <Picker.Item label="Below 10th" value="0" />
                    <Picker.Item label="10-12th" value="1" />
                    <Picker.Item label="Bachelor's" value="2" />
                    <Picker.Item label="Master's" value="3" />
                    <Picker.Item label="PhD" value="4" />
                  </Picker>
                </View>
              </View>

              <View style={styles.formGroup}>
                <Text style={styles.label}>School Type</Text>
                <View style={styles.pickerContainer}>
                  <Picker
                    selectedValue={schoolType}
                    onValueChange={setSchoolType}
                    style={styles.picker}
                  >
                    <Picker.Item label="Public" value="public" />
                    <Picker.Item label="Private" value="private" />
                  </Picker>
                </View>
              </View>
            </View>

            <TouchableOpacity
              style={styles.predictButton}
              onPress={handlePredict}
              disabled={loading}
            >
              {loading ? (
                <ActivityIndicator color="#fff" />
              ) : (
                <>
                  <MaterialCommunityIcons name="brain" size={20} color="#fff" />
                  <Text style={styles.predictButtonText}>Predict Result</Text>
                </>
              )}
            </TouchableOpacity>
          </>
        ) : (
          <View style={styles.resultContainer}>
            <View
              style={[
                styles.resultCard,
                result.prediction === 'PASS'
                  ? styles.passCard
                  : styles.failCard,
              ]}
            >
              <MaterialCommunityIcons
                name={result.prediction === 'PASS' ? 'check-circle' : 'close-circle'}
                size={60}
                color={result.prediction === 'PASS' ? '#28a745' : '#dc3545'}
              />
              <Text style={styles.resultTitle}>{result.prediction}</Text>
              <Text style={styles.resultSubtitle}>
                {result.prediction === 'PASS'
                  ? 'Student is likely to pass'
                  : 'Student is at risk of failing'}
              </Text>
            </View>

            <View style={styles.probabilitiesContainer}>
              <View style={styles.probabilityBox}>
                <Text style={styles.probabilityLabel}>Pass Probability</Text>
                <Text style={[styles.probabilityValue, styles.passText]}>
                  {result.pass_probability}%
                </Text>
              </View>
              <View style={styles.probabilityBox}>
                <Text style={styles.probabilityLabel}>Fail Probability</Text>
                <Text style={[styles.probabilityValue, styles.failText]}>
                  {result.fail_probability}%
                </Text>
              </View>
            </View>

            <TouchableOpacity
              style={styles.newPredictionButton}
              onPress={resetForm}
            >
              <Text style={styles.newPredictionButtonText}>New Prediction</Text>
            </TouchableOpacity>
          </View>
        )}
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
  section: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginBottom: 15,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '700',
    color: '#333',
    marginBottom: 15,
  },
  formGroup: {
    marginBottom: 20,
  },
  label: {
    fontSize: 14,
    fontWeight: '600',
    color: '#333',
    marginBottom: 8,
  },
  input: {
    borderWidth: 2,
    borderColor: '#e0e0e0',
    borderRadius: 8,
    padding: 12,
    fontSize: 14,
    color: '#333',
    backgroundColor: '#f9f9f9',
  },
  hint: {
    fontSize: 12,
    color: '#999',
    marginTop: 5,
  },
  pickerContainer: {
    borderWidth: 2,
    borderColor: '#e0e0e0',
    borderRadius: 8,
    overflow: 'hidden',
    backgroundColor: '#f9f9f9',
  },
  picker: {
    height: 50,
  },
  predictButton: {
    backgroundColor: '#667eea',
    padding: 15,
    borderRadius: 10,
    flexDirection: 'row',
    justifyContent: 'center',
    alignItems: 'center',
    marginTop: 10,
  },
  predictButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '700',
    marginLeft: 10,
  },
  resultContainer: {
    backgroundColor: '#fff',
    borderRadius: 15,
    padding: 20,
    marginTop: 20,
  },
  resultCard: {
    alignItems: 'center',
    paddingVertical: 30,
    borderRadius: 15,
    marginBottom: 20,
  },
  passCard: {
    backgroundColor: '#d4edda',
  },
  failCard: {
    backgroundColor: '#f8d7da',
  },
  resultTitle: {
    fontSize: 28,
    fontWeight: '700',
    marginTop: 15,
    color: '#333',
  },
  resultSubtitle: {
    fontSize: 14,
    color: '#666',
    marginTop: 10,
  },
  probabilitiesContainer: {
    flexDirection: 'row',
    gap: 15,
    marginBottom: 20,
  },
  probabilityBox: {
    flex: 1,
    backgroundColor: '#f9f9f9',
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
  },
  probabilityLabel: {
    fontSize: 12,
    color: '#999',
    marginBottom: 8,
  },
  probabilityValue: {
    fontSize: 20,
    fontWeight: '700',
  },
  passText: {
    color: '#28a745',
  },
  failText: {
    color: '#dc3545',
  },
  newPredictionButton: {
    backgroundColor: '#667eea',
    padding: 15,
    borderRadius: 10,
  },
  newPredictionButtonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '700',
    textAlign: 'center',
  },
});
