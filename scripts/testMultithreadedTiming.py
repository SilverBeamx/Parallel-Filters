import shlex
from subprocess import Popen, PIPE

word_amount = 10000000
max_threads = 30
runs = 30

def reset_log():
    with open("log/threadedTiming.csv","w") as f:
        f.write("wordAmount,threadAmount,milliSeconds\n")

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

def main():

    #Ensure that the latest version has been compiled
    print(f"> Compiling latest version")
    compile_multithreaded()

    #Wipe the log
    print(f"> Wiping the log")
    reset_log()

    #Generate an initial 10000000 elements list
    print(f"> Generating a {word_amount} words list")
    generate_wordlist(word_amount)

    #Take the timings
    for num_threads in range(1,max_threads+1):
        print(f"> Running with {num_threads} threads")
        for run_num in range(1,runs+1):
            print(f">> Run {run_num}/{runs} with {num_threads} threads")
            get_multithreaded_timing(num_threads)

if __name__ == '__main__':
    main()
