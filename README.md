# LEARN SESAME

A Django App for appreciating how [`django-sesame`](https://django-sesame.readthedocs.io/) works.


# WHAT I LEARNT

The main wand you'll want to wield is `sesame.utils.get_query_string()`

+ Create a quick-login query string for the `user` viz `sesame.utils.get_query_string(user)`
+ Attach this to a link you want the user to use as an entry point to your site
+ When the user clicks on that link, the sesame middleware reads the attached
  query string and logs the user corresponding to the value of the `sesame` key
  in the query string into the session
  (make sure sesame's model backend is in your list of backends)
+ It then redirects to the same endpoint, but without the query string (to keep
  it somewhat secure)
+ The user can then access any other endpoint on your app as a logged in user
  without need to attach the query string


# WHY I DID THIS

I was unsure of a couple of things, the most pressing of which was whether the
query string (containing the sesame authentication token) had to be passed
to every URL for the user.

I found the answer to be NO!
