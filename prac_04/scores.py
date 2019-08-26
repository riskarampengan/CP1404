def main():
    """Read and display student scores from scores file."""
    scores_file = open("scores.csv")
    scores_data = scores_file.readlines()
    print(scores_data)
    subjects = scores_data[0].strip().split(",")
    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        score_values.append(score_numbers)
    scores_file.close()
    scores_by_subjects = reorganise_score(score_values)
    subject_details(scores_by_subjects, subjects)


def reorganise_score(score_values):
    subject_scores = []
    number_of_subjects = len(score_values[0])
    for _ in range(number_of_subjects):
        scores_for_a_subject = []
        for scores in score_values:
            scores_for_a_subject.append(scores.pop(0))
        subject_scores.append(scores_for_a_subject)
    return subject_scores

def subject_details(scores_by_subjects, name_of_subject):
    for i, scores_for_a_subject in enumerate(scores_by_subjects):
        print(name_of_subject[i], "Scores: ")
        for score in scores_for_a_subject:
            print("{:>2}".format(score))
        print("Max: {:3}".format(max(scores_for_a_subject)))
        print("Min: {:3}".format(min(scores_for_a_subject)))
        print("Avg: {:6.2f}\n".format((sum(scores_for_a_subject) / len(scores_for_a_subject))))

main()