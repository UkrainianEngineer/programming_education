""" returns a dictionary with the following format:
create_dict(N)
{1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, …, N:N^2}. """


def create_dict(n):
    return {item: item ** 2 for item in range(1, n+1)}


print(create_dict(1000))
