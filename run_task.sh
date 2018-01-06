echo 'jobs dmas'
python search_google_trends.py 'jobs' DMAs > jobs_dma.log
echo 'jobs state'
python search_google_trends.py 'jobs' state > jobs_state.log

echo 'skills dmas'

python search_google_trends.py 'skills' DMAs > jobs_dma.log

echo 'skills state'

python search_google_trends.py 'skills' state > jobs_state.log

echo 'terms dmas'

python search_google_trends.py terms DMAs > jobs_dma.log

echo 'terms state'

python search_google_trends.py terms state > jobs_state.log