import os
import shlex
from subprocess import Popen, PIPE

word_start = 1000
word_end = 10000000
word_multiplier = 100
max_threads = 25
runs = 20

def reset_log():
    with open("log/threadedTiming.csv","w") as f:
        f.write("wordAmount,threadAmount,microSeconds\n")

def run_command(command):
    process = Popen(shlex.split(command), stdout=PIPE)
    (output, err) = process.communicate()
    exit_code = process.wait()
    return output, err, exit_code

def compile_multithreaded():
    command = "make bin/threadedBloom.exe"
    return run_command(command)

def generate_wordlist(word_amount):
    command = f"python ./scripts/generateFruitWordlist.py -n {word_amount}"
    return run_command(command)

def get_multithreaded_timing(num_threads):
    command = f"./bin/threadedBloom.exe -n {num_threads} -l"
    return run_command(command)

def get_multithreaded_timing_windows(num_threads):
    command = f"./x64/Release/Parallel-Filters.exe -n {num_threads} -l"
    return run_command(command)

def is_windows():
    return os.name == 'nt'

def main():

    #Ensure that the latest version has been compiled
    if not is_windows():
        print(f"> Compiling latest version")
        compile_multithreaded()

    #Wipe the log
    print(f"> Wiping the log")
    reset_log()

    word_amount = word_start
    while word_amount <= word_end:
        #Generate the initial elements list
        print(f"> Generating a {word_amount} words list")
        generate_wordlist(word_amount)

        #Take the timings
        for num_threads in range(1,max_threads+1):
            print(f"> Running with {num_threads} threads and {word_amount} words")
            for run_num in range(1,runs+1):
                print(f">> Run {run_num}/{runs} with {num_threads} threads and {word_amount} words")
                if is_windows():
                    get_multithreaded_timing_windows(num_threads)
                else:
                    get_multithreaded_timing(num_threads)

        #Increment words counter
        word_amount *= word_multiplier

if __name__ == '__main__':
    main()
