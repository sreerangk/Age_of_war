# Medieval Battle

This is a fun strategy-based simulation where you act as a medieval king deciding which of your army platoons should battle the opponent's — with the goal to win **at least 3 out of 5 battles** (or all 5 if possible!).


## Problem Summary

You and your opponent each have 5 platoons, with:
- A **unit class** (e.g. Spearmen, Militia, etc.)
- A **number of soldiers**

Some unit classes have **advantages** over others (e.g. Spearmen > Light Cavalry), giving you a 2x fighting power.

Your task: **reorder your platoons** so that your army wins at least **3 out of 5** battles.

## Unit Class Advantages

- Militia → Spearmen, LightCavalry  
- Spearmen → LightCavalry, HeavyCavalry  
- LightCavalry → FootArcher, CavalryArcher  
- HeavyCavalry → Militia, FootArcher, LightCavalry  
- CavalryArcher → Spearmen, HeavyCavalry  
- FootArcher → Militia, CavalryArcher

> If a class has an advantage, one soldier fights as two.

---

## How to Run
git clone this repo
install requirements.txt 
python manage.py runserver


Tech Stack
Python 3

Django (if backend used)

HTML + Bootstrap (for frontend)

Optional: JavaScript

<img width="1663" height="943" alt="image" src="https://github.com/user-attachments/assets/30d2eb95-edd6-4ea8-a656-ca8d3929b3b8" />

<img width="1674" height="947" alt="image" src="https://github.com/user-attachments/assets/328562c3-cfab-49cf-bd29-637b65b2dbfe" />

