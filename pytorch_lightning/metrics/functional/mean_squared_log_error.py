# Copyright The PyTorch Lightning team.
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

import torch
from deprecate import void
from torchmetrics.functional import mean_squared_log_error as _mean_squared_log_error

from pytorch_lightning.metrics.utils import deprecated_metrics


@deprecated_metrics(target=_mean_squared_log_error)
def mean_squared_log_error(preds: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
    """
    .. deprecated::
        Use :func:`torchmetrics.functional.mean_squared_log_error`. Will be removed in v1.5.0.
    """
    return void(preds, target)
