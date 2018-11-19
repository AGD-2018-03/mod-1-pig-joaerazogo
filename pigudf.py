
@outputSchema("word:chararray")
def concatenar(word1, word2):
    return (word1 + '@' + word2)

%%pig

y = FOREACH u GENERATE myudf.concatenar(firstname, surname);
DUMP y;