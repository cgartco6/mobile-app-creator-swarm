#!/usr/bin/env python3
"""
Component Library Manager - Standalone module for Mobile App Creator.
Manages reusable UI components, assets, themes with versioning and export.
"""

import json
import os
from typing import Dict, Any, List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ComponentLibraryManager:
    """Manages a library of reusable components for mobile apps."""

    def __init__(self, library_dir: str = "component_library"):
        self.library_dir = library_dir
        os.makedirs(self.library_dir, exist_ok=True)
        self.components = self._load_library()
        logger.info("ComponentLibraryManager initialized.")

    def _load_library(self) -> Dict:
        index_path = os.path.join(self.library_dir, "index.json")
        if os.path.exists(index_path):
            with open(index_path, "r") as f:
                return json.load(f)
        return {"components": {}, "themes": {}, "assets": {}}

    def _save_library(self):
        index_path = os.path.join(self.library_dir, "index.json")
        with open(index_path, "w") as f:
            json.dump(self.components, f, indent=2)

    def add_component(self, name: str, code: str, platform: str = "react_native", 
                     props: List[str] = None, description: str = "") -> Dict[str, Any]:
        """Add a new reusable component."""
        if props is None:
            props = []
        
        component = {
            "name": name,
            "platform": platform,
            "code": code,
            "props": props,
            "description": description,
            "version": "1.0.0"
        }
        
        self.components["components"][name] = component
        self._save_library()
        
        self._export_component(name, code, platform)
        logger.info(f"Added component: {name}")
        return {"status": "success", "component": component}

    def get_component(self, name: str) -> Optional[Dict]:
        """Retrieve a component."""
        return self.components["components"].get(name)

    def list_components(self) -> List[str]:
        """List all components."""
        return list(self.components["components"].keys())

    def _export_component(self, name: str, code: str, platform: str):
        """Export component to files."""
        comp_dir = os.path.join(self.library_dir, name)
        os.makedirs(comp_dir, exist_ok=True)
        
        ext = ".js" if platform == "react_native" else ".dart"
        with open(os.path.join(comp_dir, f"{name}{ext}"), "w") as f:
            f.write(code)
        
        with open(os.path.join(comp_dir, "metadata.json"), "w") as f:
            json.dump({"name": name, "platform": platform}, f, indent=2)

    def add_theme(self, name: str, colors: Dict, fonts: Dict) -> Dict:
        """Add a design theme."""
        self.components["themes"][name] = {"colors": colors, "fonts": fonts}
        self._save_library()
        return {"status": "success", "theme": name}

    def search_components(self, query: str) -> List[Dict]:
        """Search components by name or description."""
        results = []
        q = query.lower()
        for comp in self.components["components"].values():
            if q in comp["name"].lower() or q in comp["description"].lower():
                results.append(comp)
        return results

    def export_library(self, format: str = "json") -> str:
        """Export entire library."""
        export_path = os.path.join(self.library_dir, f"library_export.{format}")
        with open(export_path, "w") as f:
            json.dump(self.components, f, indent=2)
        return export_path

if __name__ == "__main__":
    manager = ComponentLibraryManager()
    
    # Demo: Add a Button component
    button_code = """import React from 'react';
import { TouchableOpacity, Text } from 'react-native';

const Button = ({ label, onPress, style }) => (
  <TouchableOpacity onPress={onPress} style={style}>
    <Text>{label}</Text>
  </TouchableOpacity>
);

export default Button;
"""
    
    result = manager.add_component(
        name="CustomButton",
        code=button_code,
        platform="react_native",
        props=["label", "onPress", "style"],
        description="Reusable themed button component"
    )
    print(json.dumps(result, indent=2))
    print("Available components:", manager.list_components())
