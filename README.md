# Unfelt Time  
A computational and scientific exploration of why humans cannot directly perceive time, even though relativity shows that time flows differently for every observer.

## Overview

Unfelt Time is a research-style machine learning and physics project that answers two high-level questions:

1. Why do humans feel space but not time.  
2. How much does time pass differently depending on where you live on Earth.

This system combines relativity, human perception modeling, neural networks, and interactive visualization to create a complete end-to-end technical project. It includes physics simulations, a city-level time dilation dataset, a trained neural model, and a Streamlit app that explains results in simple language.

The central idea is simple:  
Time is a real dimension in physics, but humans cannot sense it directly. We only notice differences in states, not the passage of time itself. This project turns that scientific idea into something measurable, visual, and interactive.

## Project Motivation

I wanted to create a project that was conceptually deep, scientifically grounded, and technically interesting. My NBA analytics and machine learning work is data driven. This project shows that I can also handle theoretical modeling, physics simulation, perception research, and interactive visualization.

The core motivation came from a question:  
If time is a dimension, why can we move around in space but not in time, and why can’t we feel its passing.

I wanted to turn that idea into a project with real datasets, real models, real visualizations, and a real interface. Unfelt Time shows I can take an abstract scientific concept and build a complete computational system around it.

## Key Features

### Physics and Perception Modeling
- Special relativity simulation for proper time vs coordinate time.
- Gravitational and velocity-based Earth time dilation calculations.
- Human perception sampling simulation demonstrating discrete consciousness frames.
- Spacetime diagram visualizations.

### Global Time Dilation Dataset
- 48,000 world cities processed from a geographic dataset.
- Added altitude and elevation features.
- Computed microseconds gained or lost per year for each city.
- Engineered features for training a neural model to predict aging rate.

### Machine Learning
- Neural network predicting aging rate from latitude, longitude, elevation.
- Synthetic and physical feature engineering.
- Model saved and served inside Streamlit.
- Real predictions shown live in the app.

### Interactive Streamlit Application

The app has two major components:

1. **City Time Dilation Explorer**  
   Allows comparison of any two cities on the planet, showing:  
   - microseconds gained or lost per year  
   - neural model prediction  
   - clear natural-language explanation from an LLM  

2. **Why Humans Cannot Feel Time**  
   Includes theory-based visualizations:  
   - physics simulations  
   - brain perception sampling  
   - spacetime worldline diagrams  
   - scientific explanations  

### Technical Depth

This project demonstrates skills in:
- Neural network modeling  
- Physics simulation with NumPy  
- Data engineering and feature construction  
- Geographic computation  
- Streamlit front-end development  
- Scientific visualization with matplotlib  
- AI explanation integration using an LLM API  



## Physics Theory Summary

### 1. Relativity Affects Time

Two factors change your rate of time passage:

1. Gravity  
2. Velocity  

Higher elevation reduces gravity, making clocks tick faster.  
Higher speed from Earth’s rotation makes clocks tick slower.

For most cities, the net effect is a few microseconds per year.

### 2. Humans Cannot Feel Time

Biological sampling blocks us from sensing time directly.

- The brain samples reality around 20 times per second.  
- Anything faster than 50 milliseconds is not consciously perceived.  
- Time itself is not sensed.  
- Only change is sensed.  

The passage of time is therefore invisible to perception.

### 3. Spacetime Locks Us Into One Direction

Humans cannot move freely in the time dimension.

We move through time at a constant rate and cannot change direction.  
This prevents direct sensing or control of the time axis.

## Visualizations Included

- Proper Time vs Coordinate Time  
- Brain Sampling vs Continuous Time  
- Spacetime Diagram  
- Neural Model Time Prediction  
- City Time Comparison  

These are automatically shown in the Streamlit app.

## How to Run

Create a virtual environment.

python -m venv .venv
source .venv/bin/activate

Install dependencies.
pip install -r requirements.txt


Run the app.
streamlit run app.py

## Summary

Unfelt Time is a complete scientific and engineering project that demonstrates:

- Physics simulation  
- Machine learning  
- Data engineering  
- Neural modeling  
- Visualization  
- Research framing  
- App deployment  
- AI explanation  

It takes a fundamental question from physics and builds an entire computational system around it. This demonstrates the ability to connect theoretical ideas with real code, real data, and real tools.


