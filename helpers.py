from typing import Any, Dict, List, Optional

def flatten_dict(nested_dict: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary.
    
    Parameters:
        nested_dict (Dict[str, Any]): The nested dictionary to flatten.
        parent_key (str, optional): The base key string to prepend to each flattened key. Defaults to ''.
        sep (str, optional): The separator for concatenating keys. Defaults to '_'.
    
    Returns:
        Dict[str, Any]: A flattened dictionary.
    """
    items = []
    for k, v in nested_dict.items():
        new_key = f'{parent_key}{sep}{k}' if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def merge_lists(list1: List[Optional[Any]], list2: List[Optional[Any]]) -> List[Optional[Any]]:
    """
    Merges two lists, preserving order.
    
    Parameters:
        list1 (List[Optional[Any]]): The first list.
        list2 (List[Optional[Any]]): The second list.
    
    Returns:
        List[Optional[Any]]: A merged list containing unique elements in order they were first encountered.
    """
    return list(dict.fromkeys(list1 + list2))


def deep_update(original: Dict[str, Any], update: Dict[str, Any]) -> Dict[str, Any]:
    """
    Recursively updates a dictionary with another dictionary.
    
    Parameters:
        original (Dict[str, Any]): The original dictionary to update.
        update (Dict[str, Any]): The dictionary with updates.
    
    Returns:
        Dict[str, Any]: The updated dictionary.
    """
    for k, v in update.items():
        if isinstance(v, dict) and k in original:
            original[k] = deep_update(original[k], v)
        else:
            original[k] = v
    return original