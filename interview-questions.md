
## 1. Fundamentals (I use this to expose fake depth)

1. What’s the difference between **MLE, MAP, and plain maximum likelihood**? When does it matter in practice?
2. Explain **bias–variance tradeoff** without textbook language. Give a real failure case.
3. Why does **cross-entropy** work better than MSE for classification?
4. When does **accuracy become a trash metric**? What do you replace it with?
5. Explain **precision–recall tradeoff** like you’re debugging a production bug.

---

## 2. Machine Learning (where weak candidates crack)

6. Walk me through **training → validation → test leakage** with a concrete example.
7. How does **regularization actually change the loss landscape**?
8. Difference between **bagging and boosting** — and don’t say “variance vs bias” unless you can prove it.
9. Why does **XGBoost often beat neural nets on tabular data**?
10. What happens if your **features drift but labels don’t**?

---

## 3. Deep Learning (no hand-waving allowed)

11. Why does **ReLU work**, and when does it absolutely fail?
12. Explain **vanishing vs exploding gradients** using math intuition.
13. What does **batch normalization** really normalize?
14. Why does **dropout hurt transformers**?
15. If your model overfits after epoch 2, what are the **first 3 things you check**?

---

## 4. NLP & LLMs (where most people bluff)

16. Explain **tokenization** and why it directly affects model cost.
17. Why do **transformers scale better than RNNs**, but also hallucinate more?
18. What exactly is **attention** doing — mathematically, not metaphorically?
19. Difference between **causal LM** and **seq2seq LM** in deployment.
20. What makes **LLMs confident but wrong**?

---

## 5. Retrieval-Augmented Generation (RAG) — I will grill you here

21. Why is **RAG not a silver bullet for hallucinations**?
22. Dense vs sparse retrieval — when does each win?
23. What is **MMR**, and why does naive top-k retrieval fail?
24. How do you evaluate a RAG system **without human labeling**?
25. Where does latency explode in RAG pipelines?

---

## 6. Agentic AI & Systems (this separates engineers from toy builders)

26. What problem do **multi-agent systems actually solve** that single-agent systems can’t?
27. When does **agent orchestration become net-negative**?
28. How do you prevent **infinite agent loops**?
29. Stateless vs stateful agents — give real consequences.
30. Why are **graphs better than chains** for complex reasoning?

---

## 7. Backend & Infrastructure (AI engineers fail here a lot)

31. Why does async FastAPI still block sometimes?
32. What happens when **LLM inference runs on the main thread**?
33. Redis vs PostgreSQL — what do you cache where, and why?
34. How do you design **idempotent AI APIs**?
35. What breaks first when 10× traffic hits your AI service?

---

## 8. Performance, Cost & Scaling (this is where money is saved)

36. Where does **LLM cost actually come from**?
37. How do you reduce inference cost **without reducing quality**?
38. What is **TTFT**, and why users care more about it than total latency?
39. How do you batch requests **without killing latency**?
40. What metrics do you put on a dashboard on day one?

---

## 9. Failure & Debugging (no hero stories)

41. Tell me about a model that **looked good offline but failed in prod**.
42. How do you detect **silent model degradation**?
43. What logs do you keep for AI systems, and why?
44. How do you debug hallucinations **systematically**?
45. What’s your rollback strategy when an LLM update breaks users?

---

## 10. Ethics, Safety & Reality Checks

46. When should you **not use an LLM**?
47. What’s the fastest way to leak user data with AI?
48. How do you prevent **prompt injection**?
49. Where does explainability matter — and where is it useless?
50. What’s one AI trend you think is **overhyped and fragile**?

---

## 11. Brutal Closing Questions (decider round)

51. If I take away **LangChain/LangGraph**, can you still build the system?
52. What part of your stack is **most replaceable**?
53. What’s the **hardest AI problem you’ve actually solved**, not talked about?
54. What would you rebuild differently if you started today?
55. Why should I hire you over someone with **2 more years of experience**?



say the word.
