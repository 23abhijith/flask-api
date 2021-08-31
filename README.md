# flask-api
Flask Api setup

# Question 1
 * Regular Expression = "^([A-Z][a-z]*(\.|-|\,|)) (([A-Z]|[a-z])[a-z]*( |\,|-|)( |)|)([A-Z][a-z]*)(.|)"
 * Where this regular expression would fail:
    * This would fail with streed names like Washington Street or other proper nounds like Eifel towers or people with a lot of middle names.

# Question 2
 * Regular Expression = "\b([A-Za-z])*([b-df-hj-np-tv-xzB-DF-HJ-NP-TV-XZ])[aeiouy][a-z]*ing\b"
 * Where this regular expression would fail:
    * This would fail for words like amazing and even fails for words such as eating. In the case of amazing it is not a true gerund as it is an adjective. On the other hand with eating the a is not preceded by a constant but it is a gerund

# Question 3
 * Regular Expression = "\([^?][^(]*\)|\(?P(<|=)[^(]*\)"
 * This regular expression would fail for (?<foo>[abc])\k<foo> since it doesnt follow the pattern of (?P<name>).
