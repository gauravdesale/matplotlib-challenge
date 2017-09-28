import matplotlib.pyplot as plt

fig, ax, = plt.subplots()
x = movie_df[movie_df.duration]
y = movie_df[movie_df.num_critic_for_review]
movie_df.hist(x, bins=20, histtype='bar', normed=True, color='BurlyWood')
movie_df.set_title("Histogram of movie data")
movie_df.set_xlabel("Duration of the movie")
movie_df.set_ylabel("Number of movie reviews")
#above is challenge one

movie_df.hist(kind='scatter', x='duration', y='number of critics')
movie_df.scatter(x, y)
#above is challenge two

x1 = movie_df(

