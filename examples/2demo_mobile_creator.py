#!/usr/bin/env python3
"""
Demo: Full Mobile App Creator Swarm Integration
"""

from ai_app_builder.ai_app_builder import AIAppBuilder
from ai_music_creator.ai_music_creator import AIMusicCreator
from ai_video_creator.ai_video_creator import AIVideoCreator
from component_library_manager.component_library_manager import ComponentLibraryManager

def main():
    print("🚀 Starting Mobile App Creator Swarm Demo\n")
    
    # 1. Build App
    app_builder = AIAppBuilder()
    app_result = app_builder.build_app("Habit tracker mobile app with streaks and social sharing")
    print(f"✅ App built: {app_result.get('app_name')}\n")
    
    # 2. Generate Music
    music = AIMusicCreator()
    song = music.generate_song("Upbeat motivational habit building track", style="electronic")
    print(f"✅ Music created: {song.get('song_name')}\n")
    
    # 3. Generate Video
    video = AIVideoCreator()
    clip = video.generate_video("Habit tracker onboarding animation with smooth transitions", duration=30)
    print(f"✅ Video clip ready: {clip.get('video_name')}\n")
    
    # 4. Component Library
    lib = ComponentLibraryManager()
    button_code = "const Button = ({label}) => <button>{label}</button>;"
    lib_result = lib.add_component("CustomButton", button_code, "react_native")
    print(f"✅ Component added: {lib_result.get('name')}\n")
    
    print("🎉 Demo completed successfully! All modules working together.")

if __name__ == "__main__":
    main()
