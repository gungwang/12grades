# -*- coding: utf-8 -*-
"""Record only hard prerequisites that high-school English truly depends on. Sequence-based soft edges are linked by the build script by volume.

Use j:<middle-school key> for middle-school prerequisites and p:<primary-school key> for primary-school prerequisites. Do not link mathematics.
Across school stages, most edges should be soft; SOFT adds extra soft edges, and hard edges are reserved for forms a topic directly requires.
"""
from en_lib import hard

SOFT = []


def soft(topic, prereq, reason):
    SOFT.append((topic, prereq, reason))

# Hard edges: later structures directly use earlier forms.
hard("gr_futcont", "j:gr_ing7", "Before using the present continuous for future plans, learn am, is, or are plus -ing.")
hard("gr_taghs", "j:gr_tag", "High-school tag questions build on the tag questions learned in middle school.")
hard("gr_relpro", "j:gr_attr", "Relative clauses with relative pronouns build on who, which, and that from middle school.")
hard("gr_relwhose", "gr_relpro", "Whose and whom are specialized uses of relative pronouns.")
hard("gr_reladv", "gr_relpro", "Learn to modify nouns with relative pronouns before studying relative adverbs.")
hard("gr_relprep", "gr_reladv", "Prepositions before relative pronouns require familiarity with both relative adverbs and pronouns.")
hard("gr_nonrest", "gr_relpro", "Learn restrictive relative clauses before nonrestrictive ones.")
hard("gr_passcont", "j:gr_pass", "The present continuous passive requires be plus a past participle.")
hard("gr_passcont", "j:gr_ing7", "The continuous passive still uses the be-plus-ing auxiliary pattern.")
hard("gr_passperf", "j:gr_pass", "The perfect passive requires familiarity with past participles in passive voice.")
hard("gr_passperf", "j:gr_pp", "The present perfect passive requires have plus a past participle.")
hard("gr_ppattr", "j:gr_pass", "See past participles in the passive voice before using them as attributive modifiers.")
hard("gr_ppcomp", "gr_ppattr", "A past participle as an object complement is the same non-finite form used attributively.")
hard("gr_ingattr", "j:gr_ger", "Using verb -ing forms attributively builds on distinguishing gerunds from other -ing forms.")
hard("gr_ingadv", "gr_ingattr", "Learn verb -ing forms as modifiers and subject complements before using them adverbially.")
hard("gr_toattr", "j:gr_to", "Using infinitives as modifiers builds on using infinitives as objects.")
hard("gr_topurp", "j:gr_purpose", "Infinitives as purpose adverbials build on the earlier use of to do to express purpose.")
hard("gr_toform", "gr_toattr", "Using an infinitive after it as a formal subject requires familiarity with infinitives.")
hard("gr_modperf", "j:gr_mustbe", "Modal verbs plus have done build on using must to express deduction.")
hard("gr_report", "j:gr_that", "Object clauses in reported speech require familiarity with that-clauses.")
hard("gr_subjcls", "j:gr_that", "That-clauses used as subjects build on object clauses learned in middle school.")
hard("gr_predcls", "gr_subjcls", "Predicative and subject clauses are both noun clauses, so learn subject clauses first.")
hard("gr_appos", "gr_predcls", "Learn noun clauses introduced by that before distinguishing appositive clauses from relative clauses.")
hard("gr_ifsubj", "j:gr_whobj", "Whether-clauses used as subjects build on the statement word order in middle-school object clauses with question words.")
hard("gr_ingperf", "gr_ingadv", "Having done is the perfect form of a verb -ing adverbial.")
hard("gr_topass", "gr_toform", "The passive infinitive builds on infinitives used as subjects and subject complements.")
hard("gr_subnow", "j:gr_if", "Counterfactual present subjunctives build on middle-school if-clauses.")
hard("gr_subpast", "gr_subnow", "Counterfactual past subjunctives build on the counterfactual present form.")
hard("gr_subpast", "j:gr_ppast", "A clause with had done requires familiarity with the past perfect.")
hard("gr_subfut", "gr_subnow", "Counterfactual future subjunctives use the same would-plus-base-form main clause.")
hard("gr_wish", "gr_subnow", "The subjunctive after wish uses the same shifted time reference as if-subjunctives.")
hard("gr_suggest", "gr_wish", "The subjunctive used for suggestions builds on special subjunctive clauses such as those after wish.")
hard("gr_invneg", "gr_subnow", "Negative-adverb inversion often appears with subjunctives and emphasis, so learn the subjunctive auxiliaries first.")
hard("gr_invonly", "gr_invneg", "Inversion with only, so, and neither is the same type of partial inversion as negative-adverb inversion.")
hard("gr_invif", "gr_subpast", "Inversion with omitted if requires familiarity with had done in counterfactual past clauses.")
hard("gr_cleft", "gr_relpro", "The that in cleft sentences can be confused with that in relative clauses, so learn relative pronouns first.")
hard("gr_doemph", "gr_cleft", "Using do to emphasize a predicate is another kind of emphasis, following sentence-pattern emphasis.")
hard("gr_ellip", "gr_toform", "When an infinitive is omitted, to remains; learn the full infinitive form first.")
hard("gr_advconc", "j:gr_although", "The concessive uses of although and while build on middle-school concessive adverbial clauses.")
hard("gr_advso", "j:gr_sothat", "So that and in case build on middle-school purpose adverbial clauses.")
hard("gr_nonfinmix", "gr_ingperf", "Comparing to do, doing, and done requires familiarity with the perfect -ing form.")
hard("gr_nonfinmix", "gr_topass", "Choosing among non-finite forms also requires familiarity with the passive infinitive.")
hard("gr_mixcls", "gr_appos", "A review of noun clauses requires distinguishing appositive clauses from relative clauses.")
hard("gr_tensemix", "j:gr_review", "Choosing tenses in connected text builds on the tense choices practiced in middle school.")

# Soft edges: connect most topics to a middle- or primary-school prerequisite, rather than relying on a single backbone.
soft("gr_sentmem", "j:gr_be7", "Before analyzing sentence elements, learn to form sentences with am, is, and are.")
soft("gr_np", "j:gr_plural7", "Noun phrases often contain plurals, so learn plural nouns before studying the whole phrase.")
soft("gr_adjp", "j:gr_comp8", "Adjective phrases can involve comparison, so learn comparative forms first.")
soft("gr_svoc", "j:gr_make", "Object-complement patterns often include make + object + verb, so learn this middle-school pattern first.")
soft("gr_used3", "j:gr_used", "Before distinguishing used to from be used to, learn used to for past habits.")
soft("gr_suggest", "j:gr_should8", "Clauses used to make suggestions express the same kind of advice as middle-school should.")
soft("gr_wouldrather", "j:gr_if", "The subjunctive use of would rather follows the shifted time reference in if-clauses.")
soft("rw_news", "j:gr_past8", "Before reading reports about past events, learn to narrate with the simple past.")
soft("ph_stresshs", "j:ph_stress", "Multisyllabic word stress builds on identifying word stress in middle school.")
soft("ph_linkhs", "j:ph_link", "High-school connected speech builds on hearing linking in middle-school phrases.")
soft("ph_pausehs", "j:ph_pause", "Pausing by sense group builds on the pauses learned in middle school.")
soft("ph_ploshs", "j:ph_plos", "Incomplete plosion builds on hearing adjacent plosive sounds in middle school.")
soft("ph_toneb", "p:ph_tone", "Rising and falling intonation at sentence ends builds on the intonation of statements and questions learned in primary school.")
soft("ph_weak", "j:ph_tone7", "Weak forms and intonation are both sentence-level sound changes, so learn sentence-final intonation first.")
soft("vo_affix", "j:gr_plural7", "Before studying how suffixes change a word's part of speech, learn the idea of changing word endings.")
