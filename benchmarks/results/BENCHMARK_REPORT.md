# KomaMRI Precompilation Benchmark Results
## v0.0.6 vs v0.0.7 Performance Comparison
| Function | v0.0.6 (s) | v0.0.7 (s) | Speedup |
|----------|-----------|-----------|----------|
| EPI_example | 8.333 | 7.469 | 1.12x |
| Phantom | 6.047 | 6.008 | 1.01x |
| Scanner | 6.051 | 5.373 | 1.13x |
| brain_phantom2D | 8.656 | 7.826 | 1.11x |
| discretize | 5.627 | 5.283 | 1.07x |
| read_phantom | 1.205 | 0.529 | 2.28x |
| simulate | 13.176 | 12.963 | 1.02x |
| write_phantom | 1.589 | 0.666 | 2.38x |

**Overall Speedup: 1.10x**
Total v0.0.6: 50.684s
Total v0.0.7: 46.117s
