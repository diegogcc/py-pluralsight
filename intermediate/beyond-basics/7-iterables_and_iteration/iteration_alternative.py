class AlternativeIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, idx):
        return self.data[idx]

if __name__ == "__main__":
    [i for i in AlternativeIterable()]
    # [1, 2, 3]