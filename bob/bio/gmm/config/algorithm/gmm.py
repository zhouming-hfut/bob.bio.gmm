#!/usr/bin/env python

import bob.bio.gmm
import numpy

algorithm = bob.bio.gmm.algorithm.GMM(
    number_of_gaussians = 512,
    # by default, features are expected to be normalized and, hence, we don't need to re-normalize them
    normalize_before_k_means = False
)
