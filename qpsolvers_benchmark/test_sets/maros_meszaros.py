#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Maros-Meszaros test set.
"""

import os.path
from typing import Dict

import yaml

from ..problem import Problem


class MarosMeszaros:

    data_dir: str
    optimal_costs: Dict[str, float]

    def __init__(self, data_dir: str):
        with open(os.path.join(data_dir, "OPTCOSTS.yaml"), "r") as fh:
            file_dict = yaml.load(fh)
            optimal_costs = {k: float(v) for k, v in file_dict.items()}
        self.data_dir = data_dir
        self.optimal_costs = optimal_costs

    def __iter__(self):
        for fname in os.listdir(self.data_dir):
            if fname.endswith(".mat"):
                mat_path = os.path.join(self.data_dir, fname)
                problem = Problem.from_mat_file(mat_path)
                if problem.name in self.optimal_costs:
                    problem.optimal_cost = self.optimal_costs[problem.name]
                yield problem