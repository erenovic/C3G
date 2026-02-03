#
# Copyright (C) 2023, Inria
# GRAPHDECO research group, https://team.inria.fr/graphdeco
# All rights reserved.
#
# This software is free for non-commercial, research and evaluation use
# under the terms of the LICENSE.md file.
#
# For inquiries contact  george.drettakis@inria.fr
#

import os

from torch.utils.cpp_extension import (
    _get_build_directory,
    load,
)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# setup(
#     name="diff_gaussian_rasterization",
#     packages=['diff_gaussian_rasterization'],
#     ext_modules=[
#         CUDAExtension(
#             name="diff_gaussian_rasterization._C",
#             sources=[
#             "cuda_rasterizer/rasterizer_impl.cu",
#             "cuda_rasterizer/forward.cu",
#             "cuda_rasterizer/backward.cu",
#             "rasterize_points.cu",
#             "ext.cpp"],
#             extra_compile_args={"nvcc": ["-I" + os.path.join(THIS_DIR, "third_party/glm/")]})
#         ],
#     cmdclass={
#         'build_ext': BuildExtension
#     }
# )

name = "diff_gaussian_rasterization"
build_dir = _get_build_directory(name, verbose=False)
_C = load(
    name=name,
    sources=[
        os.path.join(THIS_DIR, "cuda_rasterizer/rasterizer_impl.cu"),
        os.path.join(THIS_DIR, "cuda_rasterizer/forward.cu"),
        os.path.join(THIS_DIR, "cuda_rasterizer/backward.cu"),
        os.path.join(THIS_DIR, "rasterize_points.cu"),
        os.path.join(THIS_DIR, "ext.cpp"),
    ],
    extra_cuda_cflags=["-I" + os.path.join(THIS_DIR, "third_party/glm/")],
)
