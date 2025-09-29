from typing import Callable, List, Optional, Dict
from dataclasses import dataclass


@dataclass
class RouteConfig:
    """Configuration for a static route."""

    path: str
    component: Callable
    title: str
    dir_meta: Optional[List] = None
    toc_data: Optional[List[Dict[str, str]]] = None


@dataclass
class ComponentConfig:
    """Configuration for a component or chart type."""

    versions: range | List[int]
    func_prefix: str
    flexgen_url: str = ""
    has_api_reference: bool = False
