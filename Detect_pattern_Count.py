Text = "CGAACTTGTAACTTGTAACTTGTATTGCCGGCCACTTGTAACTTGTAGACACTTGTACAGTTTTACTTGTAACTTGTAATACTTGTATCATGGCACTTGTAACTTGTAGACTTGTACACGACAGGACTTGTAACTTGTACGTAACTTGTAACTTGTACACTTGTAACTTACTTGTAACTTGTAATTCCACTTGTACTGACTTGTAACTTGTACACTTGTAACTTGTAGTGACTTGTAAACTTGTAAATACTTGTAACTTGTAGAAAGACTTGTAGATGGAACTAGACTTGTACTACTTGTAACTTGTAACACTTGTAGGACTTGTACTATTACTTGTAACTTGTAACTACTTGTAAGAACTTGTAGTCCAGACTTGTAACTTGTAGGGAGAGGACTTGTAACTTGTAACTTGTAAAACTTGTAAACTTGTAGTACTTGTATGATTACTTGTAGAACTTGTAACTTGTAACTTGTATTACTTGTAACTTGTATACTTGTACCGACTTGTAACTTGTAAAAAATCGACTTGTAACTTGTAAGATACGAACTTGTAAAACTTGTAACTTGTAACTTGTAGACTTGTAAACTTGTATTTCTTCTCAACTTGTACACAACTTGTAGGAAACTTGTACATACTTGTACTACTTGTACGTGTATACTTGTAAGGTGGTCACTTGTAACTTGTATCTACTTGTAACTTGTAATACTTGTAAGAACTTGTAGACTTGTACACTTGTAAACTTGTATAACTTGTAACTTGTATACTTGTAACTTGTAAAACTTGTAAGTAGGGGTTTACTTGTAACTTGTAACTTGTAACTTGTAGTGTTGAACTTGTAAGACTTGTAACTTGTAGCACTTGTAAGCTACTTGTAACTTGTAACTTGTATTCGAGAGACTTGTATACTTGTATACTTGTAAGAAACTTGTAGCACTTACTTGTACAACTTGTAGTACTTGTAAGACTTGTATACTTGTATTGTACTTGTA"
Pattern = "ACTTGTAAC"
def repeats(Text, Pattern):
    Count = 0
    for i in range(len(Text) - len(Pattern)):
        if Text[i:i+len(Pattern)] == Pattern:
            Count = Count + 1
    return Count
print(repeats(Text, Pattern))