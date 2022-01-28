# Lab01_SDS

-Matriz de Confusion:

                 precision    recall  f1-score   support

    phishing       0.94      0.94      0.94      1737
    legitimate     0.94      0.94      0.94      1692

    accuracy                           0.94      3429
    macro avg       0.94      0.94      0.94      3429
    weighted avg    0.94      0.94      0.94      3429

Tanto las metricas de presicion, recall y f1 mostraron el mismo resultado: un 94% en el nivel de acertacion. Esto significa que cualquiera de estas metricas puede utilizarse para un modelo de arboles de desicion para deteccion de phishing.




1. ¿Cuál es el impacto de clasificar un sitio legítimo como Pishing?  
- El sitio legitimo puede ser bloqueado por varios antivirus, lo que significaria perdidas de visitas y economicas apra la empresa, asi como manchar la reputacion de esta.

2. ¿Cuál es el impacto de clasificar un sitio de Pishing como legítimo? 
- Este sitio so sera blopqueado por ningun antivirus, lo que significa que mucha gente podria entrar a este sitio y caer facilmente en la trampa.

3. En base a las respuestas anteriores, ¿Qué métrica elegiría para comparar modelos similares 
de clasificación de pishing? 
- Se elegiria la metrica de Recall, ya que generaliza sobre las caracteristicas de los enlaces legitimos/phishing en bvase al modelo.

4. ¿Es necesaria la intervención de una persona humana en la decisión final de clasificación? 
- No, si se tiene un modelo bien entrenado con una metrica acorde a la situacion, no es necesaria la intervencion humana.
