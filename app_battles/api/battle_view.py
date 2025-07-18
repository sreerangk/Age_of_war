from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from app_battles.api.battle_logic import get_detailed_analysis, solve_battle_problem
from app_battles.forms import BattleForm
from itertools import permutations
import json

from app_battles.models import Battle

class BattleView(View):
    def get(self, request):
        form = BattleForm()
        recent_battles = Battle.objects.all()[:10]
        return render(request, 'battles/index.html', {
            'form': form,
            'recent_battles': recent_battles
        })
    
    def post(self, request):
        form = BattleForm(request.POST)
        if form.is_valid():
            my_platoons = form.cleaned_data['my_platoons']
            opponent_platoons = form.cleaned_data['opponent_platoons']
            
            # Solve the battle
            result = solve_battle_problem(my_platoons, opponent_platoons)
            detailed_result = get_detailed_analysis(my_platoons, opponent_platoons)
            
            # Save to database
            battle = Battle.objects.create(
                user=request.user if request.user.is_authenticated else None,
                my_platoons=my_platoons,
                opponent_platoons=opponent_platoons,
                result=result
            )
            
            return render(request, 'battles/result.html', {
                'result': result,
                'detailed_result': detailed_result,
                'my_platoons': my_platoons,
                'opponent_platoons': opponent_platoons
            })
        
        return render(request, 'battles/index.html', {'form': form})

@method_decorator(csrf_exempt, name='dispatch')
class BattleAPIView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            my_platoons = data.get('my_platoons', '')
            opponent_platoons = data.get('opponent_platoons', '')
            
            result = solve_battle_problem(my_platoons, opponent_platoons)
            detailed_result = get_detailed_analysis(my_platoons, opponent_platoons)
            
            return JsonResponse({
                'success': True,
                'result': result,
                'detailed_result': detailed_result
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
