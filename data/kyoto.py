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
import numpy as np

import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler



# Name the iPOPO component factory
@ComponentFactory("data_kyoto")
# This component provides a dictionary service
@Provides("data_kyoto_service")
# It is the LogisticRegression
@Property("_name", "name", "kyoto")
# Automatically instantiate a component when this factory is loaded
@Instantiate("data_kyoto_instance")
class Data(object):
    """
    Implementation of a model Service LogisticRegression.
    """
    using_features = ['_DestinationPortNumber_', '_SourcePortNumber_',
                      '_Service_', '_Count_', '_SerrorRate_', '_DstHostCount_',
                      '_DstHostSRVCount_', '_DstHostSameSRCPortRate_', '_SameSRVRate_',
                      '_Label_', '_StartTime_']

    def __init__(self):
        """
        Declares members, to respect PEP-8.
        """
        self.kyoto_df = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here

        print('Start working with data of kyoto')

        all_csv_files = []
        self.kyoto_df = pd.DataFrame()

        for item in os.walk('../ModelManager/Kyoto2007'):
            for f in item[-1]:
                if f[-1:-5:-1][::-1] == '.csv':
                    all_csv_files.append('/'.join([item[0], f]))

        for csv_file in all_csv_files:
            self.kyoto_df = pd.read_csv(csv_file, sep='\t')
            try:
                self.kyoto_df['_DurationOfConnection_']
            except KeyError:
                pass  # its fine
            else:
                self.kyoto_df = self.kyoto_df.append(self.kyoto_df)

        self.kyoto_df = self.kyoto_df[self.using_features]

        self.kyoto_df['_Label_'] = self.kyoto_df['_Label_'].apply(lambda x: -1 if x < 0 else 1)
        self.kyoto_df['_StartTime_'] = pd.to_datetime(self.kyoto_df['_StartTime_'])

        self.kyoto_df['_StartTime_'] = self.kyoto_df['_StartTime_'].apply(lambda x: (x.timestamp()))

        self.kyoto_df['_StartTime_'] = StandardScaler().fit_transform(self.kyoto_df['_StartTime_'].values.reshape(-1, 1))

        self.kyoto_df['_Service_'] = LabelEncoder().fit_transform(self.kyoto_df['_Service_'])

        print('A Kyoto Data has been added successful')

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        self.kyoto_df = None

    def get_data(self, p_attacks=-1, time=True):
        if p_attacks == -1:
            df_send = self.kyoto_df
        else:
            df_1 = self.kyoto_df[self.kyoto_df['_Label_'] == 1]
            df_not1 = self.kyoto_df[self.kyoto_df['_Label_'] != 1][:int(len(df_1)*p_attacks)]
            df_send = df_1.append(df_not1)
        if time:
            return df_send
        else:
            return df_send.drop(['_StartTime_'])




