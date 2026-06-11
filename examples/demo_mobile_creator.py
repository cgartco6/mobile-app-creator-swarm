#!/usr/bin/env python3
"""
Full Integration Demo for Mobile App Creator Swarm
Demonstrates orchestration of multiple modules.
"""

import json

# Import all major modules
try:
    from ai_app_builder.ai_app_builder import AIAppBuilder
    from ai_music_creator.ai_music_creator import AIMusicCreator
    from ai_video_creator.ai_video_creator import AIVideoCreator
    from component_library_manager.component_library_manager import ComponentLibraryManager
    from blockbuster_movie_creator.blockbuster_movie_creator import BlockbusterMovieCreator
except ImportError as e:
    print(f"⚠️ Import error: {e}. Run 'pip install -e' for each module first.")
    exit(1)

def main():
    print("🚀 Starting Full Mobile App Creator Swarm Demo\n")
    
    # 1. App Builder
    print("=== AI App Builder ===")
    app_builder = AIAppBuilder()
    app_result = app_builder.build_app(
        prompt="Habit tracker mobile app with user auth, streaks, progress charts, and social sharing",
        features=["auth", "charts", "social"]
    )
    print(json.dumps(app_result, indent=2))
    print()
    
    # 2. Music Creator
    print("=== AI Music Creator ===")
    music_creator = AIMusicCreator()
    song_result = music_creator.generate_song(
        prompt="Upbeat motivational track for habit building app",
        duration=180,
        style="electronic",
        mood="energetic"
    )
    print(json.dumps({k: v for k, v in song_result.items() if k in ["song_name", "status", "style"]}, indent=2))
    print()
    
    # 3. Video Creator
    print("=== AI Video Creator ===")
    video_creator = AIVideoCreator()
    video_result = video_creator.generate_video(
        prompt="Smooth onboarding animation for habit tracker app with motivational visuals",
        duration=45,
        style="cinematic"
    )
    print(json.dumps({k: v for k, v in video_result.items() if k in ["video_name", "status", "shots"]}, indent=2))
    print()
    
    # 4. Component Library
    print("=== Component Library Manager ===")
    lib_manager = ComponentLibraryManager()
    button_code = """import React from 'react';
import { TouchableOpacity, Text, StyleSheet } from 'react-native';

const CustomButton = ({ label, onPress, style }) => {
  return (
    <TouchableOpacity onPress={onPress} style={[styles.button, style]}>
      <Text style={styles.text}>{label}</Text>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: { padding: 15, backgroundColor: '#007AFF', borderRadius: 8 },
  text: { color: 'white', textAlign: 'center' }
});

export default CustomButton;
"""
    comp_result = lib_manager.add_component(
        name="MotivationalButton",
        code=button_code,
        platform="react_native",
        props=["label", "onPress", "style"],
        description="Reusable button for habit tracker actions"
    )
    print(json.dumps(comp_result, indent=2))
    print()
    
    # 5. Blockbuster Movie (bonus)
    print("=== Blockbuster Movie Creator ===")
    movie_creator = BlockbusterMovieCreator()
    movie_result = movie_creator.create_movie("Habit tracker success story", genre="inspirational")
    print(f"Movie title: {movie_result.get('title')}")
    
    print("\n🎉 FULL SWARM DEMO COMPLETED SUCCESSFULLY!")
    print("All modules working together in the Mobile App Creator ecosystem.")

if __name__ == "__main__":
    main()
