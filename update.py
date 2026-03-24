import sys
import re
import json

raw_text = r"""1. Consumer behaviour primarily helps marketers understand how buyers _________ among the competing brands.
a. manufacture products
b. feel, think, and choose
c. evaluate competitors
d. set market prices
Answer: b. feel, think, and choose
2. Which among the following is NOT considered an environmental influence on consumer decision-making?
a. Culture
b. Family
c. Subculture
d. Personal investments
Answer: d. Personal investments
3. The stage in which a consumer seeks information from memory or external sources is called __________.
a. Need recognition
b. Information search
c. Purchase decision
d. Post-purchase evaluation
Answer: b. Information search
4. Consumers who prefer premium brands but actively look for discounts and value deals are best described as:
a. Socialites
b. Value-conscious buyers
c. Innovators
d. Laggards
Answer: b. Value-conscious buyers
5. Webrooming refers to a buying practice where consumers:
a. Inspect products online but purchase offline
b. Inspect products offline but purchase online
c. Buy only through mobile apps
d. Avoid all online information
Answer: a. Inspect products online but purchase offline
6. A shift from joint family structures to nuclear families indicates movement from:
a. Individualism to collectivism
b. Collectivism to individualism
c. Standardisation to customisation
d. Profit orientation to value orientation
Answer: b. Collectivism to individualism
7. Which consumer group is most likely to demand time-saving household products due to lifestyle constraints?
a. Elderly consumers
b. Working women
c. Teenagers
d. Retired professionals
Answer: b. Working women
8. Technological advancement has increased the importance of __________ in influencing purchase decisions.
a. Traditional billboards
b. Electronic word-of-mouth
c. Paper catalogues
d. In-store sampling only
Answer: b. Electronic word-of-mouth
9. Under the Consumer Protection Act, a claim exceeding ₹1 crore must be filed with the:
a. State Commission
b. District Forum
c. National Commission
d. Consumer Mediation Cell
Answer: c. National Commission
10. When consumers continue to question their purchase choice after buying a product, they experience:
a. High involvement learning
b. Cognitive dissonance
c. Selective retention
d. Demand contraction
Answer: b. Cognitive dissonance
11–20
11. Which among the following correctly represents the five levels of Maslow’s hierarchy?
a. Subsistence, Protection, Affection, Esteem, Creation
b. Physiological, Safety, Social, Esteem, Self-actualisation
c. Biological, Cognitive, Social, Identity, Freedom
d. Safety, Esteem, Nurturance, Autonomy, Growth
Answer: b. Physiological, Safety, Social, Esteem, Self-actualisation
12. Max-Neef’s “Subsistence” need category primarily focuses on:
a. Luxury consumption and status reinforcement
b. Food, shelter, and physical well-being
c. Freedom of expression and autonomy
d. Skill development and creativity
Answer: b. Food, shelter, and physical well-being
13. The need for Achievement, Exhibition, and Recognition falls under which cluster of Murray’s psychogenic needs?
a. Power needs
b. Information needs
c. Affection needs
d. Ambition needs
Answer: d. Ambition needs
14. According to Dichter’s Consumption Motives, the desire to impress others or attract attention relates to:
a. Cognizance
b. Exhibition
c. Autonomy
d. Nurturance
Answer: b. Exhibition
15. High-involvement purchases characterised mainly by rational evaluation (e.g., buying a house) fall under which FCB Grid quadrant?
a. Low involvement – Feel
b. High involvement – Feel
c. High involvement – Think
d. Low involvement – Think
Answer: c. High involvement – Think
16. In the FCB Grid, products purchased out of habit (e.g., biscuits, detergents) typically follow which sequence?
a. Learn → Feel → Do
b. Feel → Learn → Do
c. Do → Learn → Feel
d. Feel → Do → Learn
Answer: c. Do → Learn → Feel
17. In Consumer Involvement, products involving low risk but strong emotional appeal (e.g., chocolates, greeting cards) are classified as:
a. High involvement – Rational
b. Low involvement – Emotional
c. Low involvement – Rational
d. High involvement – Emotional
Answer: b. Low involvement – Emotional
18. Perception is best described as a process of:
a. Storing information without interpretation
b. Selecting, organising, and interpreting sensory inputs
c. Responding automatically to stimuli
d. Remembering messages exactly as delivered
Answer: b. Selecting, organising, and interpreting sensory inputs
19. The minimum level of a stimulus required for a consumer to consciously notice it is known as:
a. Differential threshold
b. Sensory saturation
c. Absolute threshold
d. Perceptual adaptation
Answer: c. Absolute threshold
20. When two attractive alternatives both appeal to a consumer (e.g., choosing between two similarly priced paint brands), the individual experiences:
a. Approach–avoidance conflict
b. Avoidance–avoidance conflict
c. Cognitive depletion
d. Approach–approach conflict
Answer: d. Approach–approach conflict
21–30
21. Personality is best described as:
a. A temporary emotional state
b. A dynamic organisation of traits influencing behaviour
c. A behaviour learned only in adulthood
d. A set of unrelated social habits
Answer: b. A dynamic organisation of traits influencing behaviour
22. Which characteristic of personality reflects the fact that no two individuals behave the same way?
a. Stability
b. Social conformity
c. Individual differences
d. Emotional neutrality
Answer: c. Individual differences
23. The Single-Trait Theory focuses on:
a. All internal traits at once
b. Only one personality trait is relevant to a specific behaviour
c. Emotional traits unrelated to consumption
d. Traits that change rapidly over time
Answer: b. Only one personality trait is relevant to a specific behaviour
24. Consumers who strongly prefer domestic products exhibit:
a. Materialism
b. Need for uniqueness
c. Ethnocentrism
d. Social character
Answer: c. Ethnocentrism
25. According to Freudian Theory, the instinctive part is:
a. Ego
b. Id
c. Superego
d. Conscious self
Answer: b. Id
26. Reality-oriented behaviour is governed by:
a. Id
b. Ego
c. Superego
d. Instinctual mind
Answer: b. Ego
27. Aggressive consumers (Horney) tend to:
a. Conform
b. Desire admiration and superiority
c. Detach
d. Avoid brands
Answer: b. Desire admiration and superiority
28. Structured planners belong to:
a. Perceiving
b. Judging
c. Sensing
d. Feeling
Answer: b. Judging
29. Brand Personality refers to:
a. Technical features
b. Human-like traits
c. Satisfaction
d. Manufacturing
Answer: b. Human-like traits
30. Meaning Transfer Model flow:
a. Product → Consumer → Celebrity
b. Brand → Consumer → Celebrity
c. Celebrity → Product/Brand → Consumer
d. Market → Brand → Celebrity
Answer: c. Celebrity → Product/Brand → Consumer
31–40
31. In the Attitude-Towards-Object (ATO) model, a consumer’s attitude is determined by:
a. The difference between ideal and actual product performance
b. The weighted sum of beliefs across salient attributes
c. The sum of brand loyalty and satisfaction
d. The importance of subjective norms alone
Answer: b. The weighted sum of beliefs across salient attributes
32. The Ideal Point Multi-Attribute Model evaluates a product based on:
a. How closely the brand matches the consumer’s ideal attribute levels
b. The number of features a product has
c. The price-to-performance ratio
d. The brand’s advertising strength
Answer: a. How closely the brand matches the consumer’s ideal attribute levels
33. Which statement correctly distinguishes the TRA (Theory of Reasoned Action) from ATO?
a. TRA ignores subjective norms completely
b. TRA includes both attitudes and social influences in predicting behaviour
c. ATO is more accurate than TRA
d. TRA focuses only on product features
Answer: b. TRA includes both attitudes and social influences in predicting behaviour
34. In TRA, subjective norms are formed by:
a. Product specifications and pricing
b. Core values and cultural beliefs
c. Normative beliefs and motivation to comply
d. Personality traits and brand experience
Answer: c. Normative beliefs and motivation to comply
35. According to the Elaboration Likelihood Model (ELM), the central route of persuasion is most effective when:
a. Product is inexpensive
b. Emotional cues dominate
c. Consumers are highly involved and motivated
d. Celebrity ads only
Answer: c. Consumers are highly involved and motivated
36. A marketer introducing a new unique feature is attempting to change attitudes by:
a. Adding a new attribute
b. Reducing attribute weights
c. Changing norms
d. Using dissonance
Answer: a. Adding a new attribute
37. Changing attribute importance is a strategy for:
a. Satisfaction
b. Altering attribute importance
c. Reducing associations
d. Group conformity
Answer: b. Altering attribute importance
38. Emotional ads influence:
a. Cognitive attitudes
b. Value-expressive attitudes
c. Behavioural attitudes
d. Utilitarian attitudes
Answer: b. Value-expressive attitudes
39. Yale Attitude Change depends on:
a. Source
b. Message
c. Audience
d. All of the above
Answer: d. All of the above
40. AKBP model sequence is:
a. Attitude → Knowledge → Behaviour → Practice
b. Awareness → Knowledge → Behaviour → Practice
c. Attention → Kinship → Belief → Participation
d. Awareness → Behaviour → Knowledge → Practice
Answer: b. Awareness → Knowledge → Behaviour → Practice
41–50
41. VALS 1 classified consumers based on:
a. Income
b. Social values and lifestyle
c. Personality
d. Demographics
Answer: b. Social values and lifestyle
42. Survivor segment is:
a. High income
b. Trendy
c. Very low income, basic needs
d. Leaders
Answer: c. Very low income, basic needs
43. Middle-class family-oriented consumers are:
a. Achievers
b. Belongers
c. Experientials
d. I-Am-Me
Answer: b. Belongers
44. VALS dimensions are:
a. Personality + age
b. Culture + motivation
c. Primary motivation + resources
d. Lifestyle + demographics
Answer: c. Primary motivation + resources
45. Innovators are:
a. Thinkers
b. Experiencers
c. Successful & sophisticated
d. Makers
Answer: c. Successful & sophisticated
46. Achievers prefer:
a. Adventure
b. Prestige products
c. Low-cost
d. Spiritual
Answer: b. Prestige products
47. Limited money but self-expression:
a. Experiencers
b. Makers
c. Strivers
d. Conscious
Answer: b. Makers
48. Festival ads reflect:
a. Product design
b. Cultural meaning transfer
c. Channel planning
d. Repositioning
Answer: b. Cultural meaning transfer
49. Sustainers prefer:
a. Luxury
b. High-tech
c. Low-priced packs
d. Designer brands
Answer: c. Low-priced packs
50. Festival gifting rituals are:
a. Grooming
b. Divestment
c. Exchange
d. Acquisition
Answer: c. Exchange
51–60
51. Celebrity defined as:
a. Product expert
b. Known outside product field
c. Social media star
d. Brand owner
Answer: b. Known outside product field
52. Rational evaluation of celebrity depends on:
a. Attractiveness
b. Knowledge & style
c. Salary
d. Ad count
Answer: b. Knowledge & style
53. Vampire effect is:
a. Decline
b. Celebrity overshadows brand
c. Multiple ads
d. Competing brands
Answer: b. Celebrity overshadows brand
54. Multi-brand endorsement issue:
a. Availability
b. Confusion
c. Pricing
d. Youth appeal
Answer: b. Confusion
55. Living with wife’s parents is:
a. Patrilocal
b. Matrilocal
c. Changing
d. Consanguine
Answer: b. Matrilocal
56. High spending on children stage:
a. Bachelor
b. Newly married
c. Full Nest II
d. Empty Nest
Answer: c. Full Nest II
57. Joint decisions increase with:
a. Low risk
b. High risk
c. Time pressure
d. Low importance
Answer: b. High risk
58. Exchange favours is:
a. Persuasion
b. Bargaining
c. Politicking
d. Rational
Answer: b. Bargaining
59. First buyers of innovation:
a. Early majority
b. Laggards
c. Innovators
d. Late adopters
Answer: c. Innovators
60. Typewriter → computer is:
a. Continuous
b. Dynamic
c. Discontinuous
d. Horizontal
Answer: c. Discontinuous
61–70
61. Adoption process is:
a. Habit
b. Uncertainty reduction
c. Loyalty
d. Pricing
Answer: b. Uncertainty reduction
62. Influences early majority:
a. Innovators
b. Early adopters
c. Late majority
d. Laggards
Answer: b. Early adopters
63. Time-saving innovation shows:
a. Compatibility
b. Observability
c. Relative advantage
d. Trialability
Answer: c. Relative advantage
64. Compatibility means:
a. Income
b. Lifestyle & values
c. Brand
d. Promotion
Answer: b. Lifestyle & values
65. Complex products adopt slowly because:
a. Cost
b. Difficult to use
c. Promotion
d. Availability
Answer: b. Difficult to use
66. Small packs improve:
a. Observability
b. Compatibility
c. Trialability
d. Advantage
Answer: c. Trialability
67. Influencers are:
a. Innovators
b. Opinion leaders
c. Followers
d. Majority
Answer: b. Opinion leaders
68. Opinion leadership is:
a. Same everywhere
b. Celebrities only
c. Product-specific
d. Controlled
Answer: c. Product-specific
69. Broad knowledge consumers are:
a. Innovators
b. Seekers
c. Market mavens
d. Early adopters
Answer: c. Market mavens
70. Two-step flow is:
a. Firm → consumer
b. Consumer → firm
c. Media → leaders → consumers
d. Retail → consumer
Answer: c. Media → leaders → consumers
71–80
71. EKB is “grand model” because:
a. Only post-purchase
b. Integrates all factors
c. Only impulse
d. Low involvement
Answer: b. Integrates all factors
72. Decision process is:
a. External
b. Feedback
c. Central component
d. Situational
Answer: c. Central component
73. Memory recall is:
a. External search
b. Selective perception
c. Internal search
d. Filtering
Answer: c. Internal search
74. Exposure → retention is:
a. Evaluation
b. Information processing
c. Need
d. Post purchase
Answer: b. Information processing
75. Considered brands are:
a. Total set
b. Awareness set
c. Evoked set
d. Rejected set
Answer: c. Evoked set
76. Motivation, personality =
a. Environment
b. Individual determinants
c. Situational
d. Feedback
Answer: b. Individual determinants
77. Performance + price value is:
a. Emotional
b. Social
c. Functional
d. Epistemic
Answer: c. Functional
78. Social approval buying is:
a. Conditional
b. Emotional
c. Social
d. Knowledge
Answer: c. Social
79. Trying new restaurant is:
a. Functional
b. Epistemic
c. Conditional
d. Ego
Answer: b. Epistemic
80. Occasion-based purchase is:
a. Emotional
b. Functional
c. Conditional
d. Social
Answer: c. Conditional"""

lines = raw_text.strip().split('\n')
questions = []
current_q = None

for line in lines:
    line = line.strip()
    if not line:
        continue
    if re.match(r'^\d+–\d+$', line):
        continue
    
    # New question
    q_match = re.match(r'^(\d+)\.\s+(.*)$', line)
    if q_match:
        if current_q:
            questions.append(current_q)
        current_q = {
            'id': q_match.group(1),
            # Preserve the Exact question string
            'question': line, 
            'options': [],
            'answer': ''
        }
        continue
        
    # Options
    opt_match = re.match(r'^([a-d])\.\s+(.*)$', line)
    if opt_match and current_q:
        current_q['options'].append(line)
        continue
        
    # Answer
    ans_match = re.match(r'^Answer:\s+([a-d])\.\s+(.*)$', line)
    if ans_match and current_q:
        current_q['answer'] = line.replace("Answer:", "").strip()
        continue
        
    # Continuation
    if current_q and len(current_q['options']) == 0 and not line.startswith('Answer:'):
        current_q['question'] += " " + line
    elif current_q and len(current_q['options']) > 0 and not line.startswith('Answer:'):
        current_q['options'][-1] += " " + line

if current_q:
    questions.append(current_q)

import json
json_data = json.dumps(questions, indent=12)

# Insert it back exactly
with open("c:\\Users\\SHIKHAR TIWARI\\Desktop\\quiz\\index.html", "r", encoding="utf-8") as f:
    text = f.read()

start_marker = "const originalQuestions = ["
end_marker = "];\n\n        let questions = [];"

start_idx = text.find(start_marker)
end_idx = text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    end_idx += 2
    new_text = text[:start_idx] + "const originalQuestions = \n" + json_data + ";" + text[end_idx:]
    with open("c:\\Users\\SHIKHAR TIWARI\\Desktop\\quiz\\index.html", "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"Updated successfully with {len(questions)} questions.")
else:
    print("Failed to find bounds.")
