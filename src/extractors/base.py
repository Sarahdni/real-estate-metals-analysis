from abc import ABC, abstractmethod
from typing import Any, Dict, List
import pandas as pd

class BaseExtractor(ABC):
    """Base class for all data extractors."""

    def __init__(self, config: Dict[str, Any]):
        """Initialize the extractor with configuration.
        
        Args:
            config: Dictionary containing configuration parameters
        """
        self.config = config
        self._validate_config()

    @abstractmethod
    def _validate_config(self) -> None:
        """Validate the configuration parameters.
        
        Raises:
            ValueError: If configuration is invalid
        """
        pass

    @abstractmethod
    def extract(self) -> pd.DataFrame:
        """Extract data from the source.
        
        Returns:
            DataFrame containing the extracted data
        
        Raises:
            ExtractionError: If data extraction fails
        """
        pass

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean the extracted data.
        
        Args:
            df: DataFrame containing the raw extracted data
        
        Returns:
            Cleaned DataFrame
        """
        # Common cleaning operations
        df = df.copy()
        df = df.dropna()  # Remove rows with missing values
        return df

class ExtractionError(Exception):
    """Custom exception for extraction errors."""
    pass