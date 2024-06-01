from abc import abstractmethod

import pandas as pd


class ClaimCreator:

    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path
        self.source_df = None
        self.output_df = None

    @abstractmethod
    def read_source_dataset(self) -> None:
        pass

    def transform_dataset(self) -> pd.DataFrame:
        self.output_df = self.source_df.apply(lambda x: self._transform_to_claims(x), axis=1)
        self._post_process_dataset()
        return self.output_df

    def _post_process_dataset(self) -> None:
        pass

    @abstractmethod
    def _transform_to_claims(self, row: pd.Series, **kwargs) -> pd.Series:
        """
        :param row: Passed from the lambda on apply
        :param kwargs: Any other args needed by the implementation
        :return: pd.Series with the new rows and make sure to set index as a list of column names
        """
        pass
