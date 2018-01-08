echo 'jobs dmas'
# python search_google_trends.py 'jobs' DMAs 1> jobs_dma.log 2> jobs_dma.log
echo 'jobs state'
# python search_google_trends.py 'jobs' state 1> jobs_state.log 2> jobs_state.log

echo 'skills dmas'

python search_google_trends.py 'skills' DMAs 1> skills_dma.log 2> skills_dma.log

echo 'skills state'

python search_google_trends.py 'skills' state 1> skills_state.log 2> skills_state.log

echo 'terms dmas'

python search_google_trends.py terms DMAs 1> terms_dma.log 2> terms_dma.log

echo 'terms state'

python search_google_trends.py terms state 2> terms_state.log 2>terms_state.log