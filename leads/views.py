from django.shortcuts import render
import pandas as pd
from geopy.geocoders import Nominatim
import folium
import time
import certifi
import ssl

ctx = ssl.create_default_context(cafile=certifi.where())
geolocator = Nominatim(user_agent="sunroute_app", ssl_context=ctx)

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        try:
            leads_df = pd.read_excel(file)
            mask = (leads_df['Data przekazania'] > start_date) & (leads_df['Data przekazania'] < end_date)
            filtered_leads = leads_df.loc[mask]
            leads_data = []
            for index, row in filtered_leads.iterrows():
                try:
                    location = geolocator.geocode(row['Kod pocztowy'], timeout=10)

                    if location:
                        lead_info = {
                            'lat': location.latitude,
                            'lon': location.longitude,
                            'name': row['Imię i nazwisko'],
                            'phone': row['Telefon'],
                            'postal_code': row['Kod pocztowy'],
                            'monthly_fee': row['Wysokość mc opłat'],
                            'placement': row['Miejsce instalacji'],
                            'when': row['Kiedy instalacja'],
                            'notes': row['Uwagi']
                        }
                        leads_data.append(lead_info)
                    else:
                        leads_data.append(None)
                except Exception as e:
                    print(f"Błąd geokodowania dla {row['Kod pocztowy']}: {e}")
        except Exception as e:
            return render(request, 'leads/upload.html', {'error': f'Błąd przetwarzania pliku: {e}'})
        return render_map(request, leads_data)
    return render(request, 'leads/upload.html')

def render_map(request, leads_data):
    m = folium.Map(location=[52.0, 19.0], zoom_start=6)

    for lead in leads_data:
        if lead['lat'] and lead['lon']:
            popup_info = f"""
                <strong>Imię i nazwisko:</strong> {lead['name']}<br>
                <strong>Telefon:</strong> {lead['phone']}<br>
                <strong>Kod pocztowy:</strong> {lead['postal_code']}<br>
                <strong>Wysokość mc opłat:</strong> {lead['monthly_fee']}<br>
                <strong>Miejsce instalacji:</strong> {lead['placement']}<br>
                <strong>Kiedy:</strong> {lead['when']}<br>
                <strong>Notatki:</strong> {lead['notes']}
            """
            folium.Marker(location=[lead['lat'], lead['lon']],
                          popup=popup_info
                          ).add_to(m)

    map_html = m._repr_html_()
    return render(request, 'leads/map.html', {'map_html': map_html})