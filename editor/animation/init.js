//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function countChainsAnimation(tgt_node, data) {

            if (! data || ! data.ext) {
                return
            }

            const input = data.in
            const explanation = data.ext.explanation
            const answer = data.ext.answer

            /*----------------------------------------------*
             *
             * attr
             *
             *----------------------------------------------*/
            const attr = {
                circle: {
                    'stroke-width': '2px',
                    'stroke': '#294270',
                    'opacity': '0.7',
                },
                grid: {
                    'stroke-width': '1px',
                    'stroke': '#82D1F5',
                },
                axis: {
                    'stroke-width': '1px',
                    'stroke': '#294270',
                    'arrow-end': 'block-wide-long',
                },
            };

            /*----------------------------------------------*
             *
             * values
             *
             *----------------------------------------------*/
            const grid_size_px = 300
            let min_height = -1
            let min_width = -1
            let max_height = 4
            let max_width = 0

            input.forEach(([x, y, r])=>{
                min_height = Math.min(min_height, y-r)
                max_height = Math.max(max_height, y+r)
                min_width = Math.min(min_width, x-r)
                max_width = Math.max(max_width, x+r)
            })

            max_height += 1
            max_width += 1
            min_height -= 1
            min_width -= 1

            const width = max_width - min_width
            const height = max_height - min_height
            const max_units = Math.max(width, height)
            const unit = grid_size_px / max_units

            if (width > height) {
                max_height = width + min_height
            } else {
                max_width = height + min_width
            }

            /*----------------------------------------------*
             *
             * paper
             *
             *----------------------------------------------*/
            const paper = Raphael(tgt_node, grid_size_px, grid_size_px, 0, 0)

            /*----------------------------------------------*
             *
             * draw grid
             *
             *----------------------------------------------*/
            // horizontal
            for (let i = 0; i <= max_units; i += 1) {
                paper.path(['M', 0, i*unit, 'h', grid_size_px]).attr(attr.grid)
            }

            // vertical
            for (let i = 0; i <= max_units; i += 1) {
                paper.path(['M', i*unit, 0, 'v', grid_size_px]).attr(attr.grid)
            }

            /*----------------------------------------------*
             *
             * draw axis
             *
             *----------------------------------------------*/
            // horizontal
            paper.path(['M', 0, (max_height)*unit, 'h', grid_size_px-4]).attr(attr.axis)

            // vertical
            paper.path(['M', (min_width*-1)*unit, grid_size_px, 'v', -grid_size_px+4]).attr(attr.axis)

            /*----------------------------------------------*
             *
             * draw circles
             *
             *----------------------------------------------*/
            let path = []
            input.forEach(([x, y, r])=>{
                paper.circle((x-min_width)*unit, (max_height-y)*unit, r*unit).attr(attr.circle)
            })

            /*----------------------------------------------*
             *
             * origin O
             *
             *----------------------------------------------*/
            const x = -min_width*unit
            const y = max_height*unit
            paper.text(x-unit/4, y+unit/4, 0).attr({'font-size': max_units/7*12})

        }

        var $tryit;

        var io = new extIO({
            multipleArguments: false,
            functions: {
                python: 'count_chains',
                js: 'countChains'
            },
            animation: function($expl, data){
                countChainsAnimation(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
