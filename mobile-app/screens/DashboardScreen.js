import React, { useState, useFocusEffect } from 'react';
import {
  View,
  ScrollView,
  Text,
  StyleSheet,
  ActivityIndicator,
  RefreshControl,
  Alert,
} from 'react-native';
import { PieChart } from 'react-native-chart-kit';
import { Dimensions } from 'react-native';
import { predictionService } from '../services/predictionService';

const screenWidth = Dimensions.get('window').width;

export default function DashboardScreen() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  useFocusEffect(
    React.useCallback(() => {
      loadStatistics();
    }, [])
  );

  const loadStatistics = async () => {
    try {
      setLoading(true);
      const response = await predictionService.getStatistics();
      if (response.statistics) {
        setStats(response.statistics);
      }
    } catch (error) {
      console.error('Error loading statistics:', error);
      Alert.alert('Info', 'Using offline data (no server connection)');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  const onRefresh = async () => {
    setRefreshing(true);
    await loadStatistics();
  };

  if (loading) {
    return (
      <View style={styles.centerContainer}>
        <ActivityIndicator size="large" color="#667eea" />
      </View>
    );
  }

  if (!stats) {
    return (
      <View style={styles.centerContainer}>
        <Text style={styles.errorText}>No data available</Text>
      </View>
    );
  }

  const passFailData = {
    labels: ['Pass', 'Fail'],
    datasets: [
      {
        data: [stats.pass_count, stats.fail_count],
      },
    ],
  };

  return (
    <ScrollView
      style={styles.container}
      refreshControl={
        <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
      }
    >
      <View style={styles.content}>
        {/* Statistics Cards */}
        <View style={styles.statsGrid}>
          <View style={styles.statCard}>
            <Text style={styles.statLabel}>Total Predictions</Text>
            <Text style={styles.statValue}>{stats.total_predictions}</Text>
          </View>

          <View style={[styles.statCard, styles.passCard]}>
            <Text style={styles.statLabel}>Passed</Text>
            <Text style={[styles.statValue, styles.passColor]}>
              {stats.pass_count}
            </Text>
          </View>

          <View style={[styles.statCard, styles.failCard]}>
            <Text style={styles.statLabel}>Failed</Text>
            <Text style={[styles.statValue, styles.failColor]}>
              {stats.fail_count}
            </Text>
          </View>

          <View style={styles.statCard}>
            <Text style={styles.statLabel}>Pass Rate</Text>
            <Text style={styles.statValue}>
              {stats.pass_rate.toFixed(1)}%
            </Text>
          </View>
        </View>

        {/* Chart */}
        <View style={styles.chartContainer}>
          <Text style={styles.chartTitle}>Pass vs Fail Distribution</Text>
          {stats.total_predictions > 0 ? (
            <PieChart
              data={passFailData}
              width={screenWidth - 40}
              height={220}
              chartConfig={{
                color: (opacity = 1) => `rgba(102, 126, 234, ${opacity})`,
                strokeWidth: 2,
              }}
              accessor={'data'}
              backgroundColor={'#fff'}
              paddingLeft={'15'}
              absolute
              colors={['#28a745', '#dc3545']}
            />
          ) : (
            <Text style={styles.noDataText}>No predictions yet</Text>
          )}
        </View>

        {/* Average Probability */}
        <View style={styles.infoCard}>
          <Text style={styles.infoTitle}>Average Pass Probability</Text>
          <View style={styles.probabilityBar}>
            <View
              style={[
                styles.probabilityFill,
                {
                  width: `${Math.min(stats.avg_pass_probability, 100)}%`,
                },
              ]}
            />
          </View>
          <Text style={styles.probabilityText}>
            {stats.avg_pass_probability.toFixed(1)}%
          </Text>
        </View>

        {/* Info Box */}
        {stats.total_predictions === 0 && (
          <View style={styles.infoBox}>
            <Text style={styles.infoBoxText}>
              No predictions yet. Go to Predictor tab to make predictions!
            </Text>
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
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  errorText: {
    fontSize: 16,
    color: '#666',
  },
  statsGrid: {
    display: 'flex',
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    marginBottom: 15,
  },
  statCard: {
    width: '48%',
    backgroundColor: '#fff',
    padding: 15,
    borderRadius: 10,
    marginBottom: 10,
    alignItems: 'center',
  },
  passCard: {
    borderTopWidth: 3,
    borderTopColor: '#28a745',
  },
  failCard: {
    borderTopWidth: 3,
    borderTopColor: '#dc3545',
  },
  statLabel: {
    fontSize: 12,
    color: '#999',
    marginBottom: 8,
  },
  statValue: {
    fontSize: 24,
    fontWeight: '700',
    color: '#667eea',
  },
  passColor: {
    color: '#28a745',
  },
  failColor: {
    color: '#dc3545',
  },
  chartContainer: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginBottom: 15,
    alignItems: 'center',
  },
  chartTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#333',
    marginBottom: 15,
  },
  noDataText: {
    fontSize: 14,
    color: '#999',
    textAlign: 'center',
    paddingVertical: 40,
  },
  infoCard: {
    backgroundColor: '#fff',
    borderRadius: 10,
    padding: 15,
    marginBottom: 15,
  },
  infoTitle: {
    fontSize: 14,
    fontWeight: '600',
    color: '#333',
    marginBottom: 10,
  },
  probabilityBar: {
    height: 10,
    backgroundColor: '#e0e0e0',
    borderRadius: 5,
    overflow: 'hidden',
    marginBottom: 8,
  },
  probabilityFill: {
    height: '100%',
    backgroundColor: '#667eea',
    borderRadius: 5,
  },
  probabilityText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#667eea',
  },
  infoBox: {
    backgroundColor: '#e7f3ff',
    borderLeftWidth: 4,
    borderLeftColor: '#2196F3',
    padding: 12,
    borderRadius: 4,
  },
  infoBoxText: {
    fontSize: 13,
    color: '#0c5aa0',
  },
});
