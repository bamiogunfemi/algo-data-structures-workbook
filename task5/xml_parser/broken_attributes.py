# C.1: Implementation
import xml.etree.ElementTree as ET
from typing import List, Dict

def find_broken_attributes(xml_file: str) -> List[Dict[str, str]]:
    """
    Recursively find broken attributes in XML document.
    
    Args:
        xml_file (str): Path to XML file
        
    Returns:
        List[Dict[str, str]]: List of dictionaries containing broken attribute details
        Each dictionary contains: path, attribute name, attribute value
    """
    broken_attrs = []
    
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        
        def check_node_attributes(node, path="") -> None:
            """
            Recursive function to check attributes of each node.
            
            Args:
                node: Current XML node being processed
                path: String representing current XML path
            """
            current_path = f"{path}/{node.tag}"
            
            for attr_name, attr_value in node.attrib.items():
                if is_attribute_broken(attr_value):
                    broken_attrs.append({
                        'path': current_path,
                        'attribute': attr_name,
                        'value': attr_value
                    })
            
            for child in node:
                check_node_attributes(child, current_path)
                
        check_node_attributes(root)
        
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return []
        
    return broken_attrs

def is_attribute_broken(value: str) -> bool:
    """
    Check if an attribute value is considered broken.
    
    Args:
        value (str): Attribute value to check
        
    Returns:
        bool: True if attribute is broken, False otherwise
    """
    if not value:  # Empty value check
        return True
    
    # Check for problematic XML characters post-parsing
    problematic_chars = ['<', '>', '&', '"', "'"]
    if any(char in value for char in problematic_chars):
        return True
    
    return False
