import React, { useEffect, useRef } from 'react';
import { View, StyleSheet, Dimensions } from 'react-native';

const ThreeDModel = () => {
  const svgRef = useRef(null);

  useEffect(() => {
    // Animated 3D-like visualization using SVG
    const svg = svgRef.current;
    if (!svg) return;

    // Create animated rotating cube-like shape
    const animate = () => {
      // This creates a visual 3D effect with SVG animation
      // We're using perspective transforms to simulate 3D
    };

    animate();
  }, []);

  // Since React Native doesn't support Three.js, we'll create an animated SVG-based 3D effect
  return (
    <View style={styles.container}>
      <svg
        width="300"
        height="300"
        viewBox="0 0 300 300"
        style={styles.svg}
      >
        <defs>
          <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#667eea" stopOpacity="1" />
            <stop offset="100%" stopColor="#764ba2" stopOpacity="1" />
          </linearGradient>
          <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#84fab0" stopOpacity="1" />
            <stop offset="100%" stopColor="#8fd3f4" stopOpacity="1" />
          </linearGradient>
        </defs>

        {/* Animated rotating shapes */}
        <g transform="translate(150, 150)">
          {/* Outer circle */}
          <circle
            cx="0"
            cy="0"
            r="100"
            fill="none"
            stroke="url(#grad1)"
            strokeWidth="2"
            opacity="0.5"
          >
            <animateTransform
              attributeName="transform"
              attributeType="XML"
              type="rotate"
              values="0;360"
              dur="20s"
              repeatCount="indefinite"
            />
          </circle>

          {/* Rotating cube faces */}
          <g>
            {/* Face 1 */}
            <polygon
              points="-50,-50 50,-50 50,50 -50,50"
              fill="url(#grad1)"
              opacity="0.7"
            >
              <animateTransform
                attributeName="transform"
                attributeType="XML"
                type="rotate"
                values="0;360"
                dur="15s"
                repeatCount="indefinite"
              />
            </polygon>

            {/* Face 2 */}
            <polygon
              points="-50,-50 50,-50 50,50 -50,50"
              fill="url(#grad2)"
              opacity="0.5"
            >
              <animateTransform
                attributeName="transform"
                attributeType="XML"
                type="rotate"
                values="0;-360"
                dur="20s"
                repeatCount="indefinite"
              />
            </polygon>

            {/* Center sphere */}
            <circle cx="0" cy="0" r="30" fill="url(#grad1)" opacity="0.8" />
            <circle cx="0" cy="0" r="25" fill="url(#grad2)" opacity="0.4" />

            {/* Orbiting particles */}
            <circle cx="60" cy="0" r="5" fill="#ffd700">
              <animateMotion dur="10s" repeatCount="indefinite">
                <mpath href="#orbit" />
              </animateMotion>
            </circle>

            <circle cx="0" cy="60" r="4" fill="#ffd700">
              <animateMotion dur="12s" repeatCount="indefinite">
                <mpath href="#orbit2" />
              </animateMotion>
            </circle>

            {/* Paths for particle motion */}
            <circle cx="0" cy="0" r="60" fill="none" id="orbit" />
            <circle cx="0" cy="0" r="60" fill="none" id="orbit2" />
          </g>

          {/* Pulsing ring */}
          <circle
            cx="0"
            cy="0"
            r="80"
            fill="none"
            stroke="url(#grad1)"
            strokeWidth="1"
            opacity="0.3"
          >
            <animate
              attributeName="r"
              values="80;120;80"
              dur="3s"
              repeatCount="indefinite"
            />
            <animate
              attributeName="opacity"
              values="0.3;0;0.3"
              dur="3s"
              repeatCount="indefinite"
            />
          </circle>
        </g>
      </svg>

      <View style={styles.textContainer}>
        <Text style={styles.title}>ScholarMind</Text>
        <Text style={styles.subtitle}>AI Powered</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  svg: {
    width: '100%',
    height: '100%',
  },
  textContainer: {
    marginTop: 20,
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#667eea',
  },
  subtitle: {
    fontSize: 14,
    color: '#666',
    marginTop: 5,
  },
});

export default ThreeDModel;
