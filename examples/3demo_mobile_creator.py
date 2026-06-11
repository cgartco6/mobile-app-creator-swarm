#!/usr/bin/env python3
"""
Demo: Full Mobile App Creator Swarm Integration
"""

try:
    from ai_app_builder.ai_app_builder import AIAppBuilder
    from ai_music_creator.ai_music_creator import AIMusicCreator
    from ai_video_creator.ai_video_creator import AIVideoCreator
    from component_library_manager.component_library_manager import ComponentLibraryManager
except ImportError as e:
    print(f"Import error: {e}. Make sure modules are installed with pip install -e .")
    exit(1)

def main():
    print("🚀 Starting Mobile App Creator Swarm Demo\n")
    
    # 1. App Builder
    app_builder = AIAppBuilder()
    app_result = app_builder.build_app("Habit tracker mobile app with streaks and social sharing")
    print(f"✅ App built: {app_result.get('app_name')}\n")
    
    # 2. Music Creator
    music = AIMusicCreator()
    song = music.generate_song("Epic motivational habit building track", style="electronic")
    print(f"✅ Music created: {song.get('song_name')}\n")
    
    # 3. Video Creator
    video = AIVideoCreator()
    clip = video.generate_video("Habit tracker onboarding animation with smooth transitions", duration=30)
    print(f"✅ Video clip ready: {clip.get('video_name')}\n")
    
    # 4. Component Library
    lib = ComponentLibraryManager()
    button_code = """import React from 'react';
import { TouchableOpacity, Text } from 'react-native';

const CustomButton = ({ label, onPress }) => (
  <TouchableOpacity onPress={onPress}>
    <Text>{label}</Text>
  </TouchableOpacity>
);

export default CustomButton;
"""
    lib_result = lib.add_component("CustomButton", button_code, "react_native", description="Reusable button")
    print(f"✅ Component added: {lib_result.get('component', {}).get('name')}\n")
    
    print("🎉 Full demo completed successfully! All modules integrated.")

if __name__ == "__main__":
    main()
