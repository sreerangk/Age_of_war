from django import forms

class BattleForm(forms.Form):
    my_platoons = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Spearmen#10;Militia#30;FootArcher#20;LightCavalry#1000;HeavyCavalry#120'
        }),
        label='Your Platoons'
    )
    
    opponent_platoons = forms.CharField(
        max_length=500,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Militia#10;Spearmen#10;FootArcher#1000;LightCavalry#120;CavalryArcher#100'
        }),
        label='Opponent Platoons'
    )
