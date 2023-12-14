# Banded-Alignment
This project compares the runtime and accuracy of standard global sequence alignment via the Needleman Wunsch algorithm to banded sequence alignment.

## Dependencies
```
pip install -r requirements.txt
```

## Running
To interact with the main functionality of the project, open 'interactive_aligner.ipynb'

To reproduce benchmarking plots:
```
cd benchmarking
py timing.py
py timing_plots.py
```

## Testing
To run the test suite simply run the following command
```
pytest
```