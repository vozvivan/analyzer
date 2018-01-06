#!/usr/bin/python3
# -- Content-Encoding: UTF-8 --
"""
This bundle provides a component that is a simple implementation of the
Model service. It contains LogisticRegression.
"""

# iPOPO decorators
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
    Validate, Invalidate, Instantiate

import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder, StandardScaler
import copy

# Name the iPOPO component factory
@ComponentFactory("data_bank_factory")
# This component provides a dictionary service
@Provides("data_bank")
# It is the LogisticRegression
@Property("_name", "name", "bank")
# Automatically instantiate a component when this factory is loaded
@Instantiate("data_bank_instance")
class Data(object):
    """
    Implementation of a model Service LogisticRegression.
    """
    using_features = ['_DestinationPortNumber_', '_SourcePortNumber_',
                      '_Service_', '_Count_', '_SerrorRate_', '_DstHostCount_',
                      '_DstHostSRVCount_', '_DstHostSameSRCPortRate_', '_SameSRVRate_',
                      '_StartTime_']

    def __init__(self):
        """
        Declares members, to respect PEP-8.
        """
        self.data = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here

        print('Start working with data of bank')

        all_csv_files = []
        df = pd.DataFrame()
        self.data = {}

        for item in os.walk('../ModelManager/sber'):
            for f in item[-1]:
                all_csv_files.append('/'.join([item[0], f]))

        for csv_file in all_csv_files:
            df = pd.read_csv(csv_file, sep='\t')
            df = df.append(df)

        df = df[df['devTime'] > 0]

        df['_StartTime_'] = StandardScaler().fit_transform(df['devTime'].values.reshape(-1, 1))
        df['_Service_'] = LabelEncoder().fit_transform(df['_Service_'])

        df['_DestinationPortNumber_'] = df['dstPort']
        df['_SourcePortNumber_'] = df['srcPort']

        features = copy.deepcopy(self.using_features)
        features.extend(['sev'])

        df = df[features].dropna()

        self.data['sev'] = df['sev']
        self.data['X_test'] = df[self.using_features]

        print('A Bank Data has been added successful')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        self.X = None
        self.y = None

    def get_data(self, **kwargs):

        return self.data

