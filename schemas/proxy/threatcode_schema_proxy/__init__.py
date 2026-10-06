"""Package exports for the ThreatCode Proxy schema artifacts."""

from importlib.resources import files

__all__ = ["__version__", "get_graphql_schema", "get_openapi_schema"]

__version__ = "0.58.3"


def get_graphql_schema() -> str:
    return files(__package__).joinpath("schema.graphql").read_text(encoding="utf-8")


def get_openapi_schema() -> str:
    return files(__package__).joinpath("openapi.yaml").read_text(encoding="utf-8")
