def bmi(cm, kg):
  cm, kg = float(cm), float(kg)
  m = cm/100
  bmi = kg/(m**2)
  idealWeight = 21*(m**2)
  return {"height":cm,"weight":kg,"bmi":round(bmi, 2),"idealWeight":round(idealWeight,2)}
