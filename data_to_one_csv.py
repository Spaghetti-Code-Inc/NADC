m_lat = [[]]
m_long = [[]]
m_h = [[]]

with open ('FY23_ADC_Latitude_PeakNearShackleton.csv', 'r') as lat:
   with open ('FY23_ADC_Longitude_PeakNearShackleton.csv', 'r') as long:
      with open ('FY23_ADC_Slope_PeakNearShackleton.csv', 'r') as h:
        
        for i, each in enumerate(lat.readlines()): 
           m_lat.append([])

           for every in each.split(','):
              m_lat[i].append(every)

        for i, each in enumerate(long.readlines()): 
            m_long.append([])

            for every in each.split(','):
                m_long[i].append(every)

        for i, each in enumerate(h.readlines()): 
            m_h.append([])

            for every in each.split(','):
                m_h[i].append(every)

with open ('PeakNearShackletonSlope.csv', 'w') as w:
    for i in range(len(m_lat)):
        for j in range(len(m_lat[i])):
            if(m_lat[i][j][-1] == '\n'): 
                m_lat[i][j] = m_lat[i][j][0:-1]
                m_long[i][j] = m_long[i][j][0:-1]
                m_h[i][j] = m_h[i][j][0:-1]
                w.write('{' + m_lat[i][j] + ':' + m_long[i][j] + ':' + m_h[i][j] + '}')
            else:
                w.write('{' + m_lat[i][j] + ':' + m_long[i][j] + ':' + m_h[i][j] + '},')

        w.write('\n')


# Format: {lat:long:height},{lat:long:height}, ...
