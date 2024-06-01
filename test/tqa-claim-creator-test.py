import unittest

import pandas as pd

from src.dataset import TQAClaimCreator


class TQAClaimCreatorTest(unittest.TestCase):

    def test_read_dataset(self):
        tcc = TQAClaimCreator('../data/TruthfulQA.csv')
        tcc.read_source_dataset()
        self.assertTrue(tcc.source_df is not None)
        self.assertEqual(tcc.source_df.columns.size, 7)

    def test_claim_transformation(self):
        tcc = TQAClaimCreator('../data/TruthfulQA.csv')
        tcc.read_source_dataset()
        transformed = tcc._transform_to_claims(tcc.source_df.loc[0])
        self.assertEqual(transformed.size, 2)
        self.assertEqual(len(transformed[0]), 14)

    def test_claim_dataset_creation(self):
        tcc = TQAClaimCreator('../data/TruthfulQA.csv')
        tcc.read_source_dataset()
        tcc.transform_dataset()
        self.assertEqual(tcc.output_df.size, 2)


if __name__ == '__main__':
    unittest.main()
