echo 'jobs dmas'
python search_google_trends.py 'jobs' DMAs 2> jobs_dma.log
echo 'jobs state'
python search_google_trends.py 'jobs' state 2> jobs_state.log

echo 'skills dmas'

python search_google_trends.py 'skills' DMAs 2> skills_dma.log

echo 'skills state'

python search_google_trends.py 'skills' state 2> skills_state.log

echo 'terms dmas'

python search_google_trends.py terms DMAs 2> terms_dma.log

echo 'terms state'

python search_google_trends.py terms state 2> terms_state.log