"""
dbapp -r all
dbapp -r brian
dbapp -w brian datadatyadat
   (could fail due to existing user)
   (ask if OK to overwrite)
dbapp -w -f brian datadatyadat
dbapp -d brian
dbapp -d all   
    (are you sure?)
"""

import sys
import os
import argparse


valid_args = ["-i",
                "--interactive",
                "-r",
                "--read",
                "w",
                "write",
                "-f",
                "--force",
                "-wf",
                "-fw",
                "-d",
                "--delete",
                ]

