from typing import List, Generator

def file_line_batches(file_path, batch_size):
    batch = []
    with open(file_path, "r") as f:
        for line in f:
            batch.append(line.rstrip("\n"))  # remove newline
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:  # yield remaining lines
            yield batch

print(next(file_line_batches("data.txt", 10)))