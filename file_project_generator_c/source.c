/*
 * {0}.c
 *
 *  Created on: ??? ?, 2022
 *      Author: llanyro
 */

#include "{0}.h"

#include "../../libs/ll_common_c.h"

void {0}_constructor({1}* {2}) {{
	assert({2} != NULL);
}}
{1}* new_{0}() {{
	{1}* {2} = ({1}*)malloc(sizeof({1}));
	{0}_constructor({2});
	return {2};
}}
void {0}_copy({1}* dest, {1}* source) {{
	assert(dest != NULL);
	assert(source != NULL);
}}
void {0}_destructor({1}* {2}) {{
	assert({2} != NULL);
}}
void delete_{0}({1}* {2}) {{
	assert({2} != NULL);
	{0}_destructor({2});
	free({2});
}}
