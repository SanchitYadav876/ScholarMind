import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import PredictorScreen from './screens/PredictorScreen';
import DashboardScreen from './screens/DashboardScreen';
import HistoryScreen from './screens/HistoryScreen';

const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

function PredictorStack() {
  return (
    <Stack.Navigator
      screenOptions={{
        headerStyle: {
          backgroundColor: '#667eea',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}
    >
      <Stack.Screen 
        name="Predictor" 
        component={PredictorScreen}
        options={{ title: 'Student Pass/Fail Predictor' }}
      />
    </Stack.Navigator>
  );
}

function DashboardStack() {
  return (
    <Stack.Navigator
      screenOptions={{
        headerStyle: {
          backgroundColor: '#667eea',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}
    >
      <Stack.Screen 
        name="Dashboard" 
        component={DashboardScreen}
        options={{ title: 'Analytics Dashboard' }}
      />
    </Stack.Navigator>
  );
}

function HistoryStack() {
  return (
    <Stack.Navigator
      screenOptions={{
        headerStyle: {
          backgroundColor: '#667eea',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}
    >
      <Stack.Screen 
        name="History" 
        component={HistoryScreen}
        options={{ title: 'Prediction History' }}
      />
    </Stack.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          headerShown: false,
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            if (route.name === 'PredictorTab') {
              iconName = focused ? 'brain' : 'brain';
            } else if (route.name === 'DashboardTab') {
              iconName = focused ? 'chart-box' : 'chart-box-outline';
            } else if (route.name === 'HistoryTab') {
              iconName = focused ? 'history' : 'history';
            }

            return <MaterialCommunityIcons name={iconName} size={size} color={color} />;
          },
          tabBarActiveTintColor: '#667eea',
          tabBarInactiveTintColor: '#999',
          tabBarStyle: {
            backgroundColor: '#fff',
            borderTopColor: '#e0e0e0',
          },
        })}
      >
        <Tab.Screen 
          name="PredictorTab" 
          component={PredictorStack}
          options={{ title: 'Predictor' }}
        />
        <Tab.Screen 
          name="DashboardTab" 
          component={DashboardStack}
          options={{ title: 'Dashboard' }}
        />
        <Tab.Screen 
          name="HistoryTab" 
          component={HistoryStack}
          options={{ title: 'History' }}
        />
      </Tab.Navigator>
    </NavigationContainer>
  );
}
