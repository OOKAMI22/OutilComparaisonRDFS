def recall():
    counter = 0
    input1 = open("Silk_key_jaro_4.nt", "r")
    input2 = open("ClefJaro4.ttl", "r")
    results_found = input1.readlines()
    true_results_found = set(input2.readlines())
    total = len(true_results_found)
    for line in results_found:
        if line in true_results_found:
            counter += 1

    print(counter, "/", total)
    return (counter / total) * 100


def precision():
    counter = 0
    input1 = open("Silk_key_jaro_4.nt", "r")
    input2 = open("ClefJaro4.ttl", "r")
    results_found = input1.readlines()
    true_results_found = set(input2.readlines())
    total = len(results_found)
    for line in results_found:
        if line in true_results_found:
            counter += 1
    print(counter, "/", total)

    return (counter / total) * 100


def fMeasure():
    prs = precision()
    rcl = recall()
    print(2 * ((prs * rcl) / (prs + rcl)))
    return 2 * ((prs * rcl) / (prs + rcl))

print(fMeasure())