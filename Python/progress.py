from tqdm import tqdm
import time

def main():
    for i in tqdm(range(100)):
        time.sleep(0.02)

if __name__ == '__main': main()
